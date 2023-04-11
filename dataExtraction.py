from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from datetime import date, datetime
from dateutil import parser
import re
from createSqliteDatabase import insert_data_into_temp_veiculo


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

def getCarBrandAndModel(description):
    # Remove digits, special characters, and extra spaces
    brand_model = re.sub(r'[\d.,/()-]', '', description).strip()
    # Remove multiple spaces
    brand_model = re.sub(r'\s{2,}', ' ', brand_model)
    # Split the string by space and take the first two words
    brand_model = brand_model.split()[:2]
    
    return brand_model

for i in range(len(ads)):
    try:
        # dscAnuncio
        description = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/h2').text
        brand, model = getCarBrandAndModel(description)
        #qtdKm
        amountKm = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[1]/span')
        #tipCambio
        gearshiftType = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[4]/span')
        #tipCombustivel
        fuelType = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/ul/li[3]/span')
        #valPreco
        price = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[2]/span')

        day, hour = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[2]/div[1]/div[2]/span[3]').text.split(',')
        #diaAnuncio
        adDate = getDate(day.lower())
        #horAnuncio
        adTime = hour
        #dscLocal
        local  = element.find_element(
            By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[2]/div[1]/div[2]/span[1]').text.split(',')
        # dscMarca
        carBrand = brand
        # dscModelo
        carModel = model

        dataAds.append((description, amountKm.text, gearshiftType.text, fuelType.text, price.text, adDate, adTime, ','.join(local), carBrand, carModel))
        # TODO: Falta fazer a paginação

    except:
        pass

insert_data_into_temp_veiculo(dataAds)
