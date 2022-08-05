import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 20)

    def Buy(self):
        # Clic on buy button
        buy_button = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
        buy_button.click()
        if not buy_button.is_displayed(): self.driver.get_screenshot_as_file("erreur_buy.png")
    def ChooseDeliveryMethod(self, index):
    # Clic on Drive pick up
        pick_up = self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".push-services--pickers li:nth-child("+str(index)+")")))
        pick_up.click()

    def EnterZipCode(self, zipcode):
        # print zip code inside text box
        input_codepostal = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[class='search-geoloc'] input[data-testid='input-control']")))
        input_codepostal.send_keys("75001")
        time.sleep(1)
        input_codepostal.send_keys(Keys.ENTER)
        if not input_codepostal.is_displayed(): self.driver.get_screenshot_as_file("erreur_zipcode.png")

    def SelectStore(self, index):
        # select first store available
        first_store = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child("+str(index)+") button")))
        first_store.click()
        if not first_store.is_displayed(): self.driver.get_screenshot_as_file("erreur_selectstore.png")

    def GetAvailabilityStatus(self):
        # Control : product is not available
        add_info = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".missing-products .ds-body-text--color-inherit")))
        return add_info.text
