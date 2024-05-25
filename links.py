from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://olx.ba/pretraga?attr=&attr_encoded=1&category_id=18&page='
path = 'edgedriver_win64/msedgedriver.exe'

options = Options()
service = Service(executable_path=path)
options.headless = True
driver = webdriver.Edge(service=service, options=options)

links = []

f = open("links_new.txt", "w")

for i in range(1, 51):
    driver.get(website + str(i))

    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cardd > a"))
    )
    
    for e in elements:
        f.write(e.get_attribute('href') + '\n')

f.close()
driver.quit()
