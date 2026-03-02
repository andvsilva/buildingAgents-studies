from chains.rag_engine import build_rag_chain

rag = build_rag_chain()

response = rag.invoke({"input": "What is ROI?"})

print(response["answer"])