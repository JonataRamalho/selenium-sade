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
import spacy

nlp = spacy.load("pt_core_news_sm")

service = Service(executable_path=ChromeDriverManager().install(), port=12345)

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-al?o=1'

driver = webdriver.Chrome(service=service)
driver.get(url)

time.sleep(10)

element = driver.find_element(By.XPATH, '//ul[@id="ad-list"]')

pagination_element = driver.find_element(By.XPATH, '//*[@id="listing-main-content-slot"]/div[13]/div/div/div[2]/div/div[2]/a')
_, total_pages = pagination_element.get_attribute("href").split('o=')

total_pages = int(total_pages)

# ads = element.find_elements(By.XPATH, '//ul[@id="ad-list"]/li')

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

# def getCarBrandAndModel(description):
#     # Remove digits, special characters, and extra spaces
#     brand_model = re.sub(r'[\d.,/()-]', '', description).strip()
#     # Remove multiple spaces
#     brand_model = re.sub(r'\s{2,}', ' ', brand_model)
#     # Split the string by space and take the first two words
#     brand_model = brand_model.split()[:2]
    
def get_brand_and_model(dscAnuncio):
    doc = nlp(dscAnuncio)

    brand, model = "não informado", "não informado"

    for token in doc:
        if token.pos_ == "PROPN":
            if brand == "não informado":
                brand = token.text
            elif model == "não informado":
                model = token.text
            else:
                break

    return brand, model

for page in range(1, total_pages + 1):
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-al?o={2}'
    driver.get(url)

    time.sleep(10)

    element = driver.find_element(By.XPATH, '//ul[@id="ad-list"]')

    ads = element.find_elements(By.XPATH, '//ul[@id="ad-list"]/li')

    for i in range(len(ads)):
        try:
            # dscAnuncio
            description = element.find_element(
                By.XPATH, '//ul[@id="ad-list"]/li['+str(i+1)+']/a/div[2]/div[1]/div[1]/h2').text
            
            brand, model = get_brand_and_model(description)
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

        except:
            pass

insert_data_into_temp_veiculo(dataAds)
