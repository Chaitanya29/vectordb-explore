import chromadb
# import uuid

client = chromadb.Client()

collection = client.get_collection(name="gym_policies")

print(f"collection: {collection}")
# print("\n In-memory Chromadb client created successfully")