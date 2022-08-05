import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


def openProducts(driver, index):
    # Function to open product by element
    if index > 0 and index <= 60:
        selector = f'.product-grid-item:not(.storetail):nth-child({index}) .product-card-image'
        product = driver.find_element(By.CSS_SELECTOR, selector)
        product.click()
    else:
        print("Index value is out of range. Should be between 1 and 60")


def openProducts2(driver, index):
    # Function to open product by list
    if index >= 0 and index < 60:
        product_list = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
        product_list[index].click()
    else:
        print("Index value is out of range. Should be between 0 and 59")


def test_carrefour():

    # Open browser and go to Web page
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    # Definition of explicit wait
    wait = WebDriverWait(driver, 10)

    # Close cookies pop up
    close_cookies = wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    close_cookies.click()

    # Clic on hamburger button
    hamburger_button = driver.find_element(By.CSS_SELECTOR, "#data-rayons")
    hamburger_button.click()

    # hover to epicerie salee
    epicerie_salee = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")))
    action.move_to_element(epicerie_salee)
    action.perform()

    # hover to feculent
    feculent = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
    action.move_to_element(feculent)
    action.perform()

    # clic on pate
    pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    pates.click()

    # Call function to open product
    # openProducts(driver, 4)
    openProducts2(driver, 3)

    # Clic on buy button
    buy_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
    buy_button.click()

    # Clic on Drive pick up
    pick_up = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")))
    pick_up.click()

    # print zip code inside text box
    zip_code = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[data-cs-mask=true]")))
    zip_code.send_keys("75001")
    time.sleep(1)
    zip_code.send_keys(Keys.ENTER)

    # select first store available
    first_store = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")))
    first_store.click()

    # Control : product is not available
    add_info = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".missing-products .ds-body-text--color-inherit")))
    assert add_info.text == "1 produit indisponible dans ce magasin."
    timestr = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f'C:\\Users\\ib\\PycharmProjects\\A4Q\\screenshots\\capture{timestr}.png'
    driver.get_screenshot_as_file(screenshot_name)
    print("Test is PASSED !!!!")

    driver.quit()