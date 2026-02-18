## Pipeline

 - Load documents
 - Parse documents
 - Chunk documents
 - Add metadata to chunks
 - Generate embeddings for chunks
 - Store embeddings in vector database
 - Receive user question
 - (Optional) Rewrite query
 - Generate embedding for question
 - Retrieve top-K similar chunks
 - (Optional) Hybrid search (vector + keyword)
 - Rerank retrieved chunks
 - Select top-N chunks
 - Build context prompt
 - Generate final answer
 - Return answer to user
