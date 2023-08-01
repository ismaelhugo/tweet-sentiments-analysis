from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

searchBrand = input("Digite o termo da busca do twitter: ")
searchBrandNoLinks = searchBrand + '-filter:links'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://twitter.com/')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
time.sleep(2)
driver.find_element(By.NAME, 'text').send_keys("IsmaelHugoDev")
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys("Soma@teste@0103")
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
time.sleep(5)

searchElement = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
searchElement.send_keys(searchBrandNoLinks)
searchElement.send_keys(Keys.RETURN)

time.sleep(3)

Tweets=[]

no_of_pagedowns = 100
elem = driver.find_element(By.XPATH, "html/body")
Tweets = []

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    try:
        articles = driver.find_elements(By.XPATH,"//*[@data-testid='tweet']")
        for article in articles:
            if article not in Tweets and len(Tweets) < 100:
                Tweets.append(article.text)
            
        no_of_pagedowns-=1
        print(Tweets)
    except:
        no_of_pagedowns-=1

def salvar_tweets_em_arquivo(tweets, nome_arquivo):
    try:
        # Verificar se o arquivo já existe e adicioná-los ao final
        with open(nome_arquivo, 'a') as arquivo:
            for tweet in tweets:
                arquivo.write(tweet + "\n \n")  # Adicionar cada tweet ao arquivo
        print("Tweets salvos com sucesso no arquivo.")
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo e salvar os tweets
        with open(nome_arquivo, 'w') as arquivo:
            for tweet in tweets:
                arquivo.write(tweet + "\n \n")  # Adicionar cada tweet ao arquivo
        print("Arquivo criado e tweets salvos com sucesso.")

nome_arquivo = "tweets.txt"

time.sleep(5)

# Chamando a função para salvar os tweets no arquivo
salvar_tweets_em_arquivo(Tweets, nome_arquivo)

time.sleep(2)