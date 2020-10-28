import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import pandas as pd


class Acoes:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe', options=options)

    def navegar(self, ativo):
        self.driver.get("https://www.fundsexplorer.com.br/funds/" + ativo)

    def valorPatrimonial(self):
        valor = self.driver.find_element_by_xpath("//*[@id='main-indicators-carousel']/div/div/div[5]/span[2]").text
        valorformatado = valor.replace("R$ ", "")
        return valorformatado

    def dividendyield(self):
        valor = self.driver.find_element_by_xpath("//*[@id='main-indicators-carousel']/div/div/div[2]/span[2]").text
        valorformatado = valor.replace("R$ ", "")
        return valorformatado

inicio = Acoes()
ativos = ["HGLG11", "XPML11"]

arquivoCsv = pd.DataFrame

for ativo in ativos:
    print(ativo)
    inicio.navegar(ativo)
    valorPatrimonial = inicio.valorPatrimonial()
    print(valorPatrimonial)
    ultimoDy = inicio.dividendyield()
    print(ultimoDy)
