import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def SetupPage(self):
        # Open browser and go to Web page
        self.driver.maximize_window()
        self.driver.get("https://www.carrefour.fr")

    def CloseCookie(self):
        # Close cookies pop up
        close_cookies = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        close_cookies.click()
    def OpenMenu(self):
        # Clic on hamburger button
        hamburger_button = self.driver.find_element(By.CSS_SELECTOR, "#data-rayons")
        hamburger_button.click()

    def OpenCategoryMenu(self,categoryMenu):
        # categoryMenu doit être exact sinon ca ne marche pas
        # hover to epicerie salee
        selector = ".nav-item__menu-link [alt='"+categoryMenu+"']"
        category = self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.action.move_to_element(category)
        self.action.perform()

    def OpenCategorySubMenu(self, index):
        # hover to feculent
        # ici on fait par index
        selector = "#data-menu-level-1_R13 > li:nth-child("+str(index)+")"
        subCategory = self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        self.action.move_to_element(subCategory)
        self.action.perform()

    def OpenProductCategoryPage(self, index):
        # clic on pate
        pates = self.driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R13F05 > li:nth-child("+str(index)+")")
        pates.click()
