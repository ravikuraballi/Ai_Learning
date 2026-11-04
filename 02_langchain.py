from langchain_ollama import chatollama
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage("you are a funny bengaluru auto driver.reply in one line."),
    HumanMessage("what is AI?")
]

model_name = "llama3.2:latest"
llm = chatollama(model=model_name)
response = llm.invoke(messages)

print(response.content)