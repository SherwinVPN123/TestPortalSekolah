from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pages import Locator, LocatorUser
from fileData import DataLoginAdmin, DataLogin, fieldAnnounc

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver.get('https://portalsiswa.id/')

def checkAnnouncment():
    loc = Locator
    dataadmin = DataLoginAdmin
    data = DataLogin
    driver.find_element(By.ID, data.loginTes).send_keys(dataadmin.namaadmin)
    driver.find_element(By.ID, data.passwordtes).send_keys(dataadmin.namapasswordadmin)
    driver.find_element(By.XPATH, loc.locatorsubmit).click()
    time.sleep(20)
    driver.find_element(By.XPATH, loc.addAnnounc).click()
    time.sleep(20)
    driver.find_element(By.XPATH, loc.tittleAnn).send_keys("Testing Judul")
    # driver.find_element(By.XPATH, loc.uploadFile).click()
    # driver.find_element(By.XPATH, loc.desCript).send_keys("Pengumuman - pengumuman")
    driver.switch_to.frame(driver.find_element(By.XPATH, loc.ifrAme))
    driver.find_element(By.XPATH, loc.desCript).send_keys("Pengumuman - pengumuman")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, loc.chooseSchool).click()
    driver.find_element(By.XPATH, loc.createButton).click()
    time.sleep(30)


def pengGuna():
    loginData = DataLogin
    datAdmin = DataLoginAdmin
    locat = Locator
    locUser = LocatorUser
    driver.find_element(By.ID, loginData.loginTes).send_keys(datAdmin.namaadmin)
    driver.find_element(By.ID, loginData.passwordtes).send_keys(datAdmin.namapasswordadmin)
    driver.find_element(By.XPATH, locat.locatorsubmit).click()
    time.sleep(20)
    driver.find_element(By.XPATH, locUser.locatorTabUser).click()
    driver.find_element(By.XPATH, locUser.locatSeeUset).click()
    time.sleep(30)
    driver.find_element(By.XPATH, locUser.inputUser).send_keys("Sherwin")
    driver.find_element(By.XPATH, locUser.buttonSearch).click()
    driver.find_element(By.XPATH, locUser.changeOpen).click()
    driver.find_element(By.XPATH, locUser.changeFirstName).send_keys("William")
    driver.find_element(By.XPATH, locUser.buttonChange).click()
    time.sleep(20)


pengGuna()

# checkAnnouncment()




