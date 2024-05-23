import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import csv

with open('links.txt', 'r') as file:
    links = file.read().splitlines()

stanje_data = []
pregledi_data = []
proizvodjac_data = []
model_data = []
gorivo_data = []
godiste_data = []
transmisija_data = []
kilometraza_data = []
kubikaza_data = []
snaga_motora_data = []
broj_vrata_data = []
cijena_data = []

def normalize_text(text):
    replacements = {
        'š': 's', 'Š': 'S',
        'č': 'c', 'Č': 'C',
        'ć': 'c', 'Ć': 'C',
        'ž': 'z', 'Ž': 'Z',
        'đ': 'dj', 'Đ': 'Dj'
    }
    for src, target in replacements.items():
        text = text.replace(src, target)
    return text

options = Options()
options.headless = True 
driver = webdriver.Edge(options=options)

for url in links:
    driver.get(url)
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    target_div = soup.find('div', class_='flex flex-row justify-start flex-wrap my-sm pb-md border-b border-gray-200')
    
    if target_div:
        labels = target_div.find_all('label', class_='btn-pill')
        
        if len(labels) > 1:
            stanje_text = labels[1].get_text(strip=True)
            stanje_data.append(normalize_text(stanje_text))
        else:
            stanje_data.append(None)
        
        if len(labels) > 4:
            fifth_text = labels[4].get_text(strip=True)
            numbers = ''.join(filter(str.isdigit, fifth_text))
            pregledi_data.append(numbers)
        else:
            pregledi_data.append(None)
    else:
        stanje_data.append(None)
        pregledi_data.append(None)
    
    attributes_div = soup.find('div', class_='required-attributes mb-lg')
    
    if attributes_div:
        for attr_div in attributes_div.find_all('div', class_='required-wrap'):
            inner_div = attr_div.find('div', class_='flex flex-col w-full')
            if inner_div:
                tds = inner_div.find_all('td')
                if len(tds) >= 2:
                    column_name = tds[0].get_text(strip=True)
                    data_text = tds[1].find('a').get_text(strip=True) if tds[1].find('a') else tds[1].get_text(strip=True)
                    normalized_text = normalize_text(data_text)
                    
                    if column_name == "Proizvođač":
                        proizvodjac_data.append(normalized_text)
                    elif column_name == "Model":
                        model_data.append(normalized_text)
                    elif column_name == "Gorivo":
                        gorivo_data.append(normalized_text)
                    elif column_name == "Godište":
                        godiste_data.append(normalized_text)
                    elif column_name == "Transmisija":
                        transmisija_data.append(normalized_text)
                    elif column_name == "Kilometraža":
                        cleaned_text = data_text.replace('.', '')
                        if cleaned_text.endswith("km"):
                            cleaned_text = cleaned_text[:-2]
                        kilometraza_data.append(cleaned_text)

                    elif column_name == "Kubikaža":
                        kubikaza_data.append(normalized_text)
                    elif column_name == "Snaga motora (KW)":
                        snaga_motora_data.append(normalized_text)
                    elif column_name == "Broj vrata":
                        broj_vrata_data.append(normalized_text)
                    else:
                        continue

        if not proizvodjac_data:
            proizvodjac_data.append(None)
        if not model_data:
            model_data.append(None)
        if not gorivo_data:
            gorivo_data.append(None)
        if not godiste_data:
            godiste_data.append(None)
        if not transmisija_data:
            transmisija_data.append(None)
        if not kilometraza_data:
            kilometraza_data.append(None)
        if not kubikaza_data:
            kubikaza_data.append(None)
        if not snaga_motora_data:
            snaga_motora_data.append(None)
        if not broj_vrata_data:
            broj_vrata_data.append(None)
    else:
        proizvodjac_data.append(None)
        model_data.append(None)
        gorivo_data.append(None)
        godiste_data.append(None)
        transmisija_data.append(None)
        kilometraza_data.append(None)
        kubikaza_data.append(None)
        snaga_motora_data.append(None)
        broj_vrata_data.append(None)

    price_elements = soup.find_all('span', class_='price-heading vat')
    price_text = None

    for price_element in price_elements:
        text = price_element.get_text(strip=True).replace('.', '').rstrip(' KM')
        if text != "Na upit":
            price_text = text
    
    if price_text is None or price_text == "Na upit":
        cijena_data.append(None)
    else:
        cijena_data.append(price_text)
driver.quit()

data = {
    'Stanje': stanje_data,
    'Pregledi': pregledi_data,
    'Cijena': cijena_data,
    'Proizvodjac': proizvodjac_data,
    'Model': model_data,
    'Gorivo': gorivo_data,
    'Godiste': godiste_data,
    'Transmisija': transmisija_data,
    'Kilometraza': kilometraza_data,
    'Kubikaza': kubikaza_data,
    'Snaga motora (KW)': snaga_motora_data,
    'Broj vrata': broj_vrata_data
}
df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)