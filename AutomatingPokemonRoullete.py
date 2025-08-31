##### 
'''
Projeto para replicar a automação criada em Automation Anywhere, para jogar o "POKEMON ROULETTE"

https://zeroxm.github.io/pokemon-roulette/
'''

'''
Na versão atual, apenas clica indefinitamente, sem ver condições.
'''
####
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print('------------INICIO -------------------')
# Inicia o navegador automaticamente com o webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://zeroxm.github.io/pokemon-roulette/")
gameend = False
while not gameend:
    try:
        wait = WebDriverWait(driver, 10)

        # Verifica se existe o botão "Click to Spin!" e clica
        try:
            spin_button = wait.until(EC.presence_of_element_located((By.XPATH, "//app-wheel//button")))
            if spin_button:
                print("Botão 'Click to Spin!' encontrado. Clicando...")
                spin_button.click()
                time.sleep(2)
        except:
            print("Botão 'Click to Spin!' não encontrado.")

        try:
            # ESCOLHE GENERO SE EXISTIR
            boy_or_girl = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main-game/div/div/div[2]/app-character-select/div/div[2]/a/img")))
            print("Clicou em Boy")
            boy_or_girl.click()
            time.sleep(2)
        except:
            print("Botão Nao Encontrado.")

        # Verifica se existe o botão "Ok" e clica
        ok_button = driver.find_element(By.XPATH, "//ngb-modal-window//button")
        if ok_button:
            print("Botão 'Ok' encontrado. Clicando...")
            ok_button.click()

    except Exception as e:
        print("Erro:", e)

driver.quit()
