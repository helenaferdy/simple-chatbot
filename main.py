import openai
openai.api_key = "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"

messages = [{"role": "user", "content": "hi there!"},]

def bot():
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    content = response['choices'][0]['message']['content']
    update_messages("assisstant",content)

    print("* BOT *")
    print(content)
    print("")

def human():
    content = input("* USER * \n")
    print("")
    update_messages("user",content)

def update_messages(role, content):
    messages.append({"role":"user", "content":content})


is_on = True
while is_on:
   bot()
   print("")
   human()