import chromadb
# import uuid

client = chromadb.PersistentClient("./chroma_db")

collection = client.get_collection(name="gym_policies")

print(f"collection: {collection.get()}")
