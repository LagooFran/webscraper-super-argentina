from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.firefox.service import Service as FService

def StartDriver():
    options = FOptions()
    driverpath = FService("drivers/geckodriver")
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, service=driverpath)
    return driver


def GetCarrefour():
    driver = StartDriver()
    driver.get("https://www.carrefour.com.ar/arroz?_q=arroz&map=ft")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    res = driver.find_elements(By.CLASS_NAME, 'valtech-carrefourar-product-summary-status-0-x-container.valtech-carrefourar-product-summary-status-0-x-productNotAdded.flex.flex-column.h-100')
    for r in res:
        print(r)
    driver.quit()
    
    
