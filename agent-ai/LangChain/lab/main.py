from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains import create_history_aware_retriever
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()


def get_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return key

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", 
                api_key=get_api_key())

# Embeddings
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# Vector DB
db = Chroma(
    collection_name="techcorp_docs",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)



retriever = db.as_retriever()

# Contextual retriever prompt
contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", "Given a chat history and the latest user question, "
            "formulate a standalone question."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# QA Prompt
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer based ONLY on the provided context:\n\n{context}"),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(
    history_aware_retriever,
    question_answer_chain
)
rag_chain = rag_chain.assign(
    output=lambda x: x["answer"]
)

# Memory store
store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

input = """ 
         Policy Summary:
         Customer personal data classified as Confidential or PII must 
         be encrypted when stored internally.

        Instructions:
        1. Identify all relevant policy rules from the retrieved context.
        2. Consider multiple possible interpretations of the policies.
        3. Evaluate each interpretation based on:
        - Security requirements
        - Data retention rules
        - Access control restrictions
        - Encryption standards
        - Compliance frameworks
        4. Eliminate interpretations not fully supported by the policy text.
        5. Select the best-supported conclusion.

        Provide your final answer structured as:

        Policy Summary:
        Technical Requirements:
        Security Controls:
        Compliance Notes:

        If the policy documents do not contain sufficient information,
        state clearly that the information is unavailable.
        """

# Invoke
response = conversational_rag.invoke(
    {"input": f"{input}"},
    config={"configurable": {"session_id": "abc123"}}
)

print(response["answer"])