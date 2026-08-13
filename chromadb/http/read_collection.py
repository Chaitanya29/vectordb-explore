import chromadb
# import uuid

client = chromadb.HttpClient(host="localhost", port=8000)

collection = client.get_collection(name="gym_policies")

print(f"collection: {collection.get()}")
