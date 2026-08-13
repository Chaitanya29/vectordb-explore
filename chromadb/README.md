# ChromaDB - A Beginner's Guide

## What is ChromaDB?

ChromaDB is an open-source vector database designed to make it easy to work with embeddings and semantic search. It's a lightweight, in-memory database that stores high-dimensional vectors (embeddings) and allows you to quickly find similar items.

## Key Concepts

### Embeddings
Embeddings are numerical representations of text, images, or other data converted into vectors. These vectors capture the semantic meaning of the data, allowing machines to understand similarity between items.

### Vector Database
A vector database is optimized for storing and searching vectors efficiently. Unlike traditional databases that work with exact matches, vector databases excel at finding "similar" items based on vector proximity.

### Semantic Search
Instead of keyword matching, semantic search understands the meaning behind queries. For example, searching for "car" might also return results for "automobile" because they're semantically similar.

## Why Use ChromaDB?

- **Simple API**: Easy to get started with minimal setup
- **Fast Similarity Search**: Quickly find similar embeddings
- **Flexible Storage**: Use in-memory or persistent storage
- **Multi-modal**: Works with text, images, and other data types
- **Perfect for Beginners**: No complex database administration needed

## Basic Use Cases

1. **Semantic Search**: Find similar documents based on meaning
2. **Recommendation Systems**: Suggest items similar to user preferences
3. **Duplicate Detection**: Identify similar or duplicate content
4. **RAG (Retrieval-Augmented Generation)**: Enhance AI models with external knowledge

## Getting Started

### Installation
```bash
pip install chromadb
```

### Simple In-Memory Client Example
```python
import chromadb

# Create a client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="documents")

# Add documents with embeddings
collection.add(
    documents=["This is a document about cats", "This is a document about dogs"],
    ids=["doc1", "doc2"]
)

# Search for similar documents
results = collection.query(
    query_texts=["Tell me about pets"],
    n_results=2
)

print(results)
```

## Summary

ChromaDB makes working with embeddings and semantic search accessible to beginners. It abstracts away complexity while providing powerful search capabilities, making it ideal for building AI-powered applications without requiring deep database expertise.

## In-Memory Client Behavior

- **Ephemeral storage:** The default `chromadb.Client()` used in the examples is an in-memory client. Collections and documents exist only in the running Python process. When the script or process exits, that in-memory data is discarded and cannot be read by a new process.
- **Reading within the same process:** While a process is running you can read collections using the same `client` instance (for example via `client.get_collection(name)`, `collection.peek()`, or `collection.query(...)`). Separate scripts (separate processes) do not share the in-memory state.
- **Common pitfall:** Running `create_collection.py` and then running a separate script like `read_collection.py` will not show the previously added documents unless both run inside the same process or you recreate the collection/data in the new run.