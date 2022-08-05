from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class ProductCategoryPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def openProductsPage(self, index):
        # Function to open product by list
        if index >= 0 and index < 60:
            product_list = self.driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
            product_list[index].click()
        else:
            print("Index value is out of range. Should be between 0 and 59")