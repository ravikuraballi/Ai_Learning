from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

response = llm.invoke("What is AI?")

print(response.content)