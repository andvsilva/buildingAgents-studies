import streamlit as st
from operator import itemgetter

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from config import get_api_key


# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Compliance RAG Assistant", page_icon="📚")

st.title("📚 Compliance RAG Assistant")


# ---------- LLM ----------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=get_api_key(),
    streaming=True
)

# ---------- EMBEDDINGS ----------
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=get_api_key()
)

# ---------- VECTOR DB ----------
db = Chroma(
    collection_name="techcorp_docs",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

retriever = db.as_retriever(search_kwargs={"k": 4})


# ---------- DOCUMENT FORMATTER ----------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ---------- PROMPT ----------
prompt = ChatPromptTemplate.from_template(
    """You are a compliance assistant.

Answer ONLY using the provided context.
If the answer is not in the context, say:
"I cannot find this information in the provided documents."

Chat History:
{chat_history}

Context:
{context}

Question:
{question}
"""
)


# ---------- SESSION MEMORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


def format_chat_history(messages):
    history = ""
    for msg in messages:
        history += f"{msg['role']}: {msg['content']}\n"
    return history


# ---------- RAG CHAIN ----------
rag_chain = (
    {
        "context": itemgetter("question") | retriever | RunnableLambda(format_docs),
        "question": itemgetter("question"),
        "chat_history": itemgetter("chat_history"),
    }
    | prompt
    | llm
)


# ---------- DISPLAY HISTORY ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------- USER INPUT ----------
if user_input := st.chat_input("Ask a compliance question..."):

    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare chat history text
    chat_history = format_chat_history(st.session_state.messages)

    # Generate response
    with st.chat_message("assistant"):
        response = rag_chain.invoke(
            {
                "question": user_input,
                "chat_history": chat_history,
            }
        )

        st.markdown(response.content)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )