#Custom chatbot written in Python using openai API

import openai

#Add GenAI API Key Here

messages = []
system_msg = input("What type of chatbot would you like to create?  ")
messages.append({"role": "system", "content": system_msg})

print("ITS ALIVE!!!!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
