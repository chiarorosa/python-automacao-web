from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "/usr/bin/google-chrome"

driver = webdriver.Chrome(options=chrome_options)

from selenium.webdriver.common.by import By


username = "email@gmail.com"
password = "teste123"

url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AVQVeywvQyYphohhtBlGL4itUsFmx2DT_hBwJnDTnj7bEkvVrkKCCnXx07CnLB3epi95vuQlfVBr&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S973681704%3A1699641728198469&theme=glif"

driver.get(url)
driver.maximize_window()

driver.find_element(By.ID, "identifierId").send_keys(username)
sleep(3)
driver.find_element(By.ID, "identifierNext").click()
sleep(10)
driver.find_element(By.NAME, "password").send_keys(password)
sleep(2)
driver.find_element(By.ID, "passwordNext").click()

print("Login realizado com sucesso!")
driver.quit()