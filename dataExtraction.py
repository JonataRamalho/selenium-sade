from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


service = Service(executable_path=ChromeDriverManager().install(), port=12345)

url = 'https://al.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios'

driver = webdriver.Chrome(service=service)
driver.get(url)

time.sleep(10)

element = driver.find_element(By.XPATH, '//ul[@id="ad-list"]')

ads = element.find_elements(By.XPATH, '//ul[@id="ad-list"]/li')

dataAds = []

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

        print(price.text)
    except:
        pass
