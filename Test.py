from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pages import Locator
from fileData import DataLogin

#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get('https://portalsiswa.id/')
# driver.find_element(By.ID,'login').send_keys("widayat")
# driver.find_element(By.ID,'password').send_keys("admankind-09")
# driver.find_element(By.XPATH,'//button[@type="submit" and text()="Masuk"]').click()
# time.sleep(5)+


def getUsernamefield():
    driver = webdriver.Chrome()
    driver.maximize_window()
    locator = Locator
    data = DataLogin
    driver.find_element(By.ID, data.loginTes).send_keys(data.namaguru)
    driver.find_element(By.ID, data.passwordtes).send_keys(data.passwordguru)
    driver.find_element(By.XPATH, locator.locatorsubmit).click()
    time.sleep(30)
    driver.find_element(By.XPATH, locator.locatorassesment).click()
    driver.find_element(By.XPATH, locator.locatorcreateassesment).click()
    time.sleep(60)
    driver.find_element(By.XPATH, locator.locatorcolomassesment).click()
    driver.find_element(By.XPATH, locator.subject).click()
    driver.find_element(By.XPATH, locator.assesmenTitle).send_keys("Testing automation")
    time.sleep(10)

def loginMurid ():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://portalsiswa.id/')
    locator = Locator
    data = DataLogin
    driver.find_element(By.ID, data.loginTes).send_keys(data.namamurid)
    driver.find_element(By.ID, data.passwordtes).send_keys(data.namapassowrdmurid)
    driver.find_element(By.XPATH, locator.locatorsubmit).click()
    time.sleep(30)


# def createAssesment():



# getUsernamefield()
loginMurid()
