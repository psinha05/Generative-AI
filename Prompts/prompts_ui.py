from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import streamlit as st
import requests
import os


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
st.header('Research Tool')
user_input = st.text_input('Enter your prompts')
result = model.invoke(user_input)

if st.button('summarize'):
    st.write(result.content) 


