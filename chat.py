import openai
import os
import json
import matplotlib.pyplot as plt

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():

    messages = []

    with open("testTweets.txt", "r") as arquivo:
       tweet = arquivo.read()

    messages.append({"role": "user", "content": "Classifique esses tweets em positivo, negativo e neutro para uma marca e retorne em um json com as chaves texto e classificacao:" + tweet})

    # Request gpt-3.5-turbo for chat completion
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    chat_message = response['choices'][0]['message']['content']

    resposta = f"{chat_message}"
    print(resposta)

    data_dict = json.loads(resposta)

    messages.append({"role": "assistant", "content": chat_message})

    quant_pos = 0
    quant_neg = 0
    quant_neu = 0
     
    try:
        for i in range(50):
           if data_dict[i]['classificacao'] == "positivo":
             quant_pos = quant_pos + 1
           elif data_dict[i]['classificacao'] == "negativo":
             quant_neg = quant_neg + 1
           else:
             quant_neu = quant_neu + 1
    except:
        for i in range(50):
           if data_dict['tweets'][i]['classificacao'] == "positivo":
             quant_pos = quant_pos + 1
           elif data_dict['tweets'][i]['classificacao'] == "negativo":
             quant_neg = quant_neg + 1
           else:
             quant_neu = quant_neu + 1

    print(quant_pos)
    print(quant_neg)
    print(quant_neu)

    labels = "Positivo", "Negativo", "Neutro"
    sizes = [quant_pos, quant_neg, quant_neu]

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    ax1.axis('equal')

    plt.show()
    

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()