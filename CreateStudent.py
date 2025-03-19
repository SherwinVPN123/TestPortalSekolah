from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pages import Locator
from fileData import DataLoginAdmin
from pages import CreateStudent
from fileData import DataLogin

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver.get('https://portalsiswa.id/')


def BuatmuridBaru():
    loc = Locator
    data = DataLoginAdmin
    BuatMurid = CreateStudent
    dataMasuk = DataLogin

    driver.find_element(By.ID, dataMasuk.loginTes).send_keys(data.namaadmin)
    driver.find_element(By.ID, dataMasuk.passwordtes).send_keys(data.namapasswordadmin)
    driver.find_element(By.XPATH, loc.locatorsubmit).click()
    time.sleep(10)
    driver.find_element(By.XPATH, BuatMurid.Skip).click()
    driver.find_element(By.XPATH, BuatMurid.clickTabuser).click()
    driver.find_element(By.XPATH, BuatMurid.clickaddnewStudent).click()
    driver.find_element(By.XPATH, BuatMurid.clickRadiobuttonStudent).click()
    driver.find_element(By.XPATH, BuatMurid.InputFirstName).send_keys("Test")
    driver.find_element(By.XPATH, BuatMurid.InputLastName).send_keys("Automation")
    driver.find_element(By.XPATH, BuatMurid.InputUserName).send_keys("TestAuth")
    driver.find_element(By.XPATH, BuatMurid.droDownClass).click()
    time.sleep(10)
    driver.find_element(By.XPATH, BuatMurid.clickClasslevel).click()
    driver.find_element(By. XPATH, BuatMurid.GetClass).click()
    time.sleep(10)
    driver.find_element(By.XPATH, BuatMurid.SellectGender).click()
    driver.find_element(By.XPATH, BuatMurid.chooseGendder).click()
    driver.find_element(By.XPATH, BuatMurid.SellectReligion).click()
    driver.find_element(By.XPATH, BuatMurid.chooseRelegion).click()
    time.sleep(20)
    driver.find_element(By.XPATH, BuatMurid.ClickChooseClass).click()
    driver.find_element(By.XPATH, BuatMurid.GetSpesificClass).click()
    driver.find_element(By.XPATH, BuatMurid.clickzerroArea).click()
    driver.find_element(By.XPATH, BuatMurid.SubmitCreateStudent).click()
    time.sleep(20)
    # driver.find_element (By.XPATH, BuatMurid.searchButton).send_keys("Automation")

def searchStudent():
    loct = Locator
    dataadmin = DataLoginAdmin
    SearchMurid = CreateStudent
    datalogin = DataLogin

    driver.find_element(By.ID, datalogin.loginTes).send_keys(dataadmin.namaadmin)
    driver.find_element(By.ID, datalogin.passwordtes).send_keys(dataadmin.namapasswordadmin)
    driver.find_element(By.XPATH, loct.locatorsubmit).click()
    time.sleep(20)
    driver.find_element(By.XPATH, SearchMurid.Skip).click()
    driver.find_element(By.XPATH, SearchMurid.clickTabuser).click()
    driver.find_element(By.XPATH, SearchMurid.User).click()
    time.sleep(10)
    driver.find_element(By.XPATH, SearchMurid.searchButton).send_keys("Automation")
    driver.find_element(By.XPATH, SearchMurid.clickSearch).click()
    time.sleep(5)
    element = driver.find_element(By.XPATH, SearchMurid.NameofStudent)  # this element is visible
    if element.is_displayed():
        print("Element found")
    else:
        print("Element not found")

    time.sleep(10)




# BuatmuridBaru()

searchStudent()
    