import ollama 

res= ollama.chat(
    model='gemma4:e2b',
    messages= [
        {
            "role":'user',
            'content':'hello, tell me a short joke.'
        }
    ]
)
# print(res)
# print(res['message'])
print(res['message']['content'])
