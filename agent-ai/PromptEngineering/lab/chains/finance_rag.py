from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


def build_finance_rag():

    # 1️⃣ Load finance documents
    loader = DirectoryLoader(
        "data/finance_docs",
        glob="**/*.txt",
        loader_cls=TextLoader
    )
    documents = loader.load()

    # 2️⃣ Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    docs = splitter.split_documents(documents)

    # 3️⃣ Embeddings
    embeddings = OpenAIEmbeddings()

    # 4️⃣ Vector DB
    vectorstore = Chroma(
        collection_name="finance_collection",
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    vectorstore.add_documents(docs)

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # 5️⃣ Controlled Finance Prompt
    template = """
You are a financial analyst AI.

Use ONLY the provided context to answer the question.

If the answer is not in the context, say:
"I don't know based on the provided financial documents."

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    llm = ChatOpenAI(model="gpt-4o-mini")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain