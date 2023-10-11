# Automação com Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import random, time, datetime

# Instanciando o serviço do navegador da versão atual
service = Service(ChromeDriverManager().install())
#service = Service(GeckoDriverManager().install())



class automatizaWeb:
    def __init__(self):
        # Instanciando o navegador
        self.browser = webdriver.Chrome(service=service)
        #self.browser = webdriver.Firefox(service=service)
    
    def abrirPagina(self, url):
        # Abrindo o navegador e acessando o site
        self.browser.get(url)

    def preencherFormulario(self):
        listaEmails = [
            "email-teste@gmail.com",
            "email-teste@outlook.com.br",
            "email-teste@yahoo.com.br",
            ]

        # Preenchendo o formulário com o e-mail
        self.browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(random.choice(listaEmails))

        listaOpcoes = [
            '//*[@id="i9"]/div[3]/div',
            '//*[@id="i12"]/div[3]/div'
        ]

        self.browser.find_element('xpath', random.choice(listaOpcoes)).click()

    
    def enviarFormulario(self):
        # Enviando o formulário
        self.browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    
    def fecharNavegador(self):
        self.browser.quit()


if __name__ == '__main__':

    # Instanciando a classe
    automatiza = automatizaWeb()

    # Defina a hora desejada (22:00 no formato de 24 horas)
    hora_desejada = datetime.time(23, 0)

    # Inicialize uma variável para rastrear a iteração
    iteracao_atual = 0

    for i in range(3000):
        
        # Abrindo o navegador
        automatiza.abrirPagina('https://forms.gle/Dn55ETCGQ6kAjkZq8')

        # Preenchendo o formulário
        automatiza.preencherFormulario()

        # Enviando o formulário
        automatiza.enviarFormulario()

        atraso = random.uniform(5, 10)

        if iteracao_atual in [100,500,1000,1500,2000,2500,3000,3500,4000,4500,5000]:
            atraso = 60
        
        print("Atraso: " + str(atraso) + " segundos")
        time.sleep(atraso)

        iteracao_atual = i

        # Obtenha a hora atual
        hora_atual = datetime.datetime.now().time()

        # Verifique se a hora atual é igual à hora desejada
        if hora_atual >= hora_desejada:
            print(f"Parou na iteração {i}...")
            break

    # Fechando o navegador
    automatiza.fecharNavegador()    