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

    def navegarfiis(self, ativo):
        self.driver.get("https://fiis.com.br/" + ativo)

    def navegarclubefii(self, ativo):
        self.driver.get("https://www.clubefii.com.br/fiis/"+ativo)

    def valorPatrimonial(self, ativo):
        self.navegarfiis(ativo)
        valor = self.driver.find_element_by_xpath("//*[@id='informations--indexes']/div[4]/span[1]").text
        valorformatado = valor.replace("R$", "")
        return valorformatado

    def dividendyield(self, ativo):
        self.navegarfiis(ativo)
        valor = self.driver.find_element_by_xpath("//*[@id='informations--indexes']/div[2]/span[1]").text
        valorformatado = valor.replace("R$", "")
        return valorformatado

    def tipoFundo(self, ativo):
        self.navegarfiis(ativo)
        valor = self.driver.find_element_by_xpath("//*[@id='informations--basic']/div[1]/div[2]/span[2]").text
        return valor

    def vacancia(self, ativo):
        self.navegarclubefii(ativo)
        try:
            vacancia = self.driver.find_element_by_xpath("//*[@id='vacancia']/div[2]/div[1]/strong[2]").text
            data_ref = self.driver.find_element_by_xpath("//*[@id='vacancia']/span").text
            return vacancia, data_ref
        except:
            vacancia = "N/A"
            data_ref = "N/A"
            return vacancia, data_ref

inicio = Acoes()
ativos = ["HGLG11", "XPML11", "MXRF11"]

arquivoCsv = pd.DataFrame

for ativo in ativos:
    print(ativo)
    valorPatrimonial = inicio.valorPatrimonial(ativo)
    print(valorPatrimonial)
    ultimoDy = inicio.dividendyield(ativo)
    print(ultimoDy)
    tipofundo = inicio.tipoFundo(ativo)
    print(tipofundo)
    vacancia = inicio.vacancia(ativo)
    print(vacancia)