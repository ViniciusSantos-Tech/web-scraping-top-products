#𝑭𝑬𝑰𝑻𝑶 𝑷𝑶𝑹 𝑽𝑰𝑵𝑰𝑪𝑰𝑼𝑺 𝑺𝑨𝑵𝑻𝑶𝑺-𝑻𝑬𝑪𝑯

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
tentativas = 3
for tentativa in range(tentativas):
    try:
        driver.get('https://www.magazinevoce.com.br/magazinetopvendasdia/?gad_source=1')
        sleep(2)
        lugar = driver.find_element(By.XPATH, '//*[@id="input-search"]')
        lugar.click()
        sleep(1)
        Escrever = lugar.send_keys("Mais vendidos")
        lugar.send_keys(Keys.ENTER)
        sleep(5)
        elementos = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[3]/div/ul/li')
        print("-----5 PRODUTOS MAIS VENDIDOS-----")
        for elemento in elementos[:5]:
            nome =  elemento.find_element(By.XPATH, './/a/div[3]/h2')
            print(f"|Produto: {nome.text}")
            print("|--------------")
        driver.quit()
        break
    except:
        print("Erro! tentando Novamente")
