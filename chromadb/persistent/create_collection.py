import chromadb
import uuid

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name="gym_policies")

with open("gym_policy.txt", "r", encoding="utf-8") as f:
    policies: list[str] = f.read().splitlines()

collection.add(
        ids = [str(uuid.uuid4()) for _ in policies ],
        documents=policies,
        metadatas=[{"line":line} for line in range(len(policies))]
    )

    # print(collection.peek())

result = collection.query(
        query_texts=[
            "Can TestGym staff ask me to provide identification?",
            "What should I do if I don't know how to use a gym machine?",
            "Can I leave weights on the gym floor after using them?",
            "Am I allowed to occupy a machine for a long time?",
            "What should I do with my personal valuables while at the gym?",
            "Is TestGym responsible if my belongings are lost or damaged?",
            "Which changing room can I use?",
            "Can I share my PIN or QR code with another person?",
          ],
        n_results=1

    )
print("len",len(result))
for i, query_res in enumerate(result["documents"]):
    print(f"\nQuery {i}")
    print(f"\n".join(query_res))
