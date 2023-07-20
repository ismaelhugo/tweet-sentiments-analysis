import openai
from dotenv import load_dotenv
import os
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
tweets = ["O site da farm é muito bugado kkkkk q ódio", "Entrei no site da farm e me endividei legal"]

string_tweets = '\n'.join(tweets)

print(string_tweets)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Classifique esses tweets em positivo, negativo e neutro para uma marca: O site da farm é muito bugado kkkkk q ódio, Entrei no site da farm e me endividei legal",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# choices = response["choices"]
# text_json = json.dumps(choices)
# ranks = []

# for choice in choices:
#     text = choice["text"]
#     ranks.append(text)

print(response)