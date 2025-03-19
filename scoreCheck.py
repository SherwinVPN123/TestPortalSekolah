from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pages import Locator
from fileData import DataLogin

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver.get('https://portalsiswa.id/')


def checkScoreStudent():
    lokasi = Locator
    datamasuk = DataLogin
    driver.find_element(By.ID, datamasuk.loginTes).send_keys(datamasuk.namamurid)
    driver.find_element(By.ID, datamasuk.passwordtes).send_keys(datamasuk.namapassowrdmurid)
    driver.find_element(By.XPATH, lokasi.locatorsubmit).click()
    time.sleep(20)
    driver.find_element(By.XPATH, lokasi.skip).click()
    time.sleep(20)
    driver.find_element(By.XPATH, lokasi.repport).click()
    driver.find_element(By.XPATH, lokasi.close).click()
    driver.find_element(By.XPATH, lokasi.bukuNilai).click()
    driver.find_element(By.XPATH, lokasi.close).click()
    time.sleep(30)

checkScoreStudent()

