import ollama
messages = [
    {
        "role":"system",
        "content":"you are funny Bengaluru auto driver.reply in one line"
    },
    {
        "role":"user",
        "content":"what is AI?"
    }

]
model_name = "llama3.2:latest"
response =ollama.chat(model = model_name,messages = messages)
print(response.message.content)