from langchain_huggingface import  HuggingFaceEmbeddings 
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about bumrah"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Convert the embeddings to numpy arrays for cosine similarity calculation
doc_embeddings_np = np.array(doc_embedding)  # Convert list of document embeddings to numpy array
query_embedding_np = np.array(query_embedding).reshape(1, -1)  # Reshape the query embedding to (1, n)

# Compute cosine similarity between the query and the documents
similarity_scores = cosine_similarity(query_embedding_np, doc_embeddings_np)[0]

index, score = sorted(list(enumerate(similarity_scores)), key= lambda x:x[1])[-1]

# Print the similarity scores
print(query)
print(documents[index])
print("Cosine Similarity Score:", score)