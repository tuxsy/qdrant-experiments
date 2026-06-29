from qdrant_client import QdrantClient, models
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def main():
    print("Hello from qdrant-experiments!")
    qdrant_url = os.getenv("QDRANT_URL")
    if not qdrant_url:
        raise ValueError("QDRANT_URL environment variable is not set. Please set it in your .env file.")
    client = QdrantClient(url=qdrant_url)
    print(f"Connected to Qdrant at {qdrant_url}")

    collections = client.get_collections()
    print(f"\nQdrant collection count: {len(collections.collections)} collections\n")
    for collection in collections.collections:
        print(f"\t- {collection.name}")

    print()


if __name__ == "__main__":
    main()
