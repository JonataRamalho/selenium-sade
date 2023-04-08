from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from datetime import date, datetime
from dateutil import parser


service = Service(executable_path=ChromeDriverManager().install(), port=12345)

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-al?o=21'

driver = webdriver.Chrome(service=service)
driver.get(url)

time.sleep(10)

element = driver.find_element(By.XPATH, '//ul[@id="ad-list"]')

ads = element.find_elements(By.XPATH, '//ul[@id="ad-list"]/li')

months = {
    'jan': 1,
    'fev': 2,
    'mar': 3,
    'abr': 4,
    'mai': 5,
    'jun': 6,
    'jul': 7,
    'ago': 8,
    'set': 9,
    'out': 10,
    'nov': 11,
    'dez': 12
}

dataAds = []


def getDate(day):
    dateToday = date.today()

    if day == 'hoje':
        return dateToday.strftime('%d/%m/%Y')
    elif day == 'ontem':
        yesterday = dateToday - datetime.timedelta(days=1)
        return yesterday.strftime('%d/%m/%Y')
    else:
        abbreviatedDay, abbreviatedMonth = day.split(' de ')
        month = months[abbreviatedMonth]
        year = datetime.today().year
        data = datetime(year, month, int(abbreviatedDay))
        return data.strftime('%d/%m/%Y')


for i in range(len(ads)):
    try:
        description = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/h2')

        amountKm = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[1]/span')

        gearshiftType = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[4]/span')

        fuelType = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[3]/span')

        price = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[2]/span')

        day, hour = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[2]/div[1]/div[2]/span[3]').text.split(',')

        announcementDate = getDate(day.lower())

        print(announcementDate)

        # TODO: Falta obter indo de local
        # TODO: Falta fazer a paginação
        # TODO: Enviar os dados para tbl_temp_veiculo

    except:
        pass
