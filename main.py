import openai
openai.api_key = "key"

messages = [{"role": "user", "content": "hi there!"},]

def bot():
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    content = response['choices'][0]['message']['content']
    update_messages("assistant",content)

    print("* BOT *")
    print(content)
    print("")

def human():
    content = input("* USER * \n")
    print("")
    update_messages("user",content)

def update_messages(role, content):
    messages.append({"role":role, "content":content})


while True:
   bot()
   human()