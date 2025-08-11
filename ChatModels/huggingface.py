from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Ensure that the token is being loaded from environment variables
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the token is correctly loaded
if not api_token:
    raise ValueError("Hugging Face API token not found. Please check your .env file.")

# Use the API token to set the Hugging Face API endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    headers={"Authorization": f"Bearer {api_token}"}  # Pass the token as a header
)

model = ChatHuggingFace(llm=llm)

# Invoke the model
result = model.invoke("What is the capital of India")

# Print the result
print(result.content)
