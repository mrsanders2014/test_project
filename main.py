"""Main module for testing ChromaDB and tiktoken functionality.

This module demonstrates:
- Creating and managing ChromaDB collections for travel policies
- Querying vector embeddings for semantic search
- Using tiktoken for token counting
"""
import chromadb
import tiktoken

SEPARATOR = "***********************************"

def main():
    print("Hello from test-project!")
    
    # Initialize the ChromaDB client. This creates an in-memory database.
    client = chromadb.Client()
    
    # Create a new collection or get it if it already exists.
    collection = client.get_or_create_collection(name="travel_policies")
    collection.add(
    ids=[
        "flight_policy_01",
        "hotel_policy_01",
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
      )
    results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2 # Ask for the top 2 most relevant results
)

    print(results)
    print(SEPARATOR)
    

    collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},
        {"policy_type": "train", "last_updated": "2025-10-15"}
    ]
)
    results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2 # Ask for the top 2 most relevant results
)   
    
    print(results)
    print("**********************")
    results = collection.query(
    query_texts=["What is the policy for booking hotels?"],
    n_results=2 # Ask for the top 2 most relevant results
)   
    print(results)
    
    # Use PersistentClient and give it a path to a folder
# This client will save all data to the "./chroma_db" directory
persistent_client = chromadb.PersistentClient(path="./chroma_db")

# Now, creating a collection works the same way, but it will be saved to disk.
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

# Data added to this collection will persist between sessions
p_collection.add(
    ids=["saved_policy_01"],
    documents=["All expense reports must be submitted within 15 days of trip completion."]
)
print("just saved the document: saved_policy_01")

 #
# By default, chromadb.Client() creates an "in-memory" database, 
# which is erased when your program finishes. 
# To save your data permanently, use the PersistentClient.
# 
# You simply provide a path to a directory where you want ChromaDB to store its files.
# If the directory doesn't exist, ChromaDB will create it.

# Use PersistentClient and give it a path to a folder
# This client will save all data to the "./chroma_db" directory
persistent_client = chromadb.PersistentClient(path="./chroma_db")

# Now, creating a collection works the same way, but it will be saved to disk.
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

# Data added to this collection will persist between sessions
p_collection.add(
    ids=["saved_policy_01"],
    documents=["All expense reports must be submitted within 15 days of trip completion."]
)

# Read (List All Collections)
# To see all collections in the database, use list_collections().
all_collections = persistent_client.list_collections()
print(SEPARATOR)
print("Available collections:")
for coll in all_collections:
    print(f"- {coll.name}")
    
    
print(SEPARATOR)
  
encoding = tiktoken.get_encoding("cl100k_base")
token_count = len(encoding.encode("This is a sample sentence."))
print(f"Token Count: {token_count}")
    



    

    
if __name__ == "__main__":
    main()
