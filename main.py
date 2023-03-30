import openai
import base64

NOT_KEY = base64.b64decode(("c2stcTNuaVhLSkRVRENoZGhRaklBNnhUM0JsYmtGSkIyb2VsdEd1ZjlwY0VVU3JvckI0").encode('utf-8')).decode('utf-8')

openai.api_key = NOT_KEY
messages = [{"role": "user", "content": "hi there!"},]

def bot():
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    content = response['choices'][0]['message']['content']
    update_messages("assistant",content)

    print("* Bot *")
    print(content)
    print("")

def human():
    content = input("* Human * \n")
    print("")
    update_messages("user",content)

def update_messages(role, content):
    messages.append({"role":role, "content":content})


while True:
   bot()
   human()