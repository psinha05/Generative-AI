from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke("Write 5 lines about black hole")

print(result.content)