from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from config import get_api_key

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=get_api_key()
)

# Embeddings
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=get_api_key()
)

# Vector DB
db = Chroma(
    collection_name="techcorp_docs",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

retriever = db.as_retriever()

# Prompt
prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the context below.

Context:
{context}

Question:
{question}
"""
)

# Build RAG pipeline
rag_chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
    }
    | prompt
    | llm
)

# Invoke
response = rag_chain.invoke(
    {"question": "What is the policy on data encryption?"}
)

print(response.content)