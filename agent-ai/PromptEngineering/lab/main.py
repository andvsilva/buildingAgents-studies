from chains.finance_rag import build_finance_rag

rag = build_finance_rag()

while True:
    question = input("\nAsk a finance question: ")

    if question.lower() == "exit":
        break

    result = rag.invoke({"query": question})

    print("\nAnswer:\n", result["result"])

    print("\nSources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata["source"])