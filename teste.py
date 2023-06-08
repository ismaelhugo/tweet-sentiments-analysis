from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://twitter.com/')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'css-4rbku5').click()
time.sleep(2)
driver.find_element(By.NAME, 'text').send_keys("IsmaelHugoDev")
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys("Soma@teste@0103")
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
time.sleep(5)

searchElement = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
searchElement.send_keys("coleção farm until:2023-06-07 since:2023-06-01")
searchElement.send_keys(Keys.RETURN)

time.sleep(3)

Tweets=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")

time.sleep(1)

while True:
    for article in articles:
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").get_attribute("innerHTML")
        time.sleep(3)
        print(Tweet)

time.sleep(30)