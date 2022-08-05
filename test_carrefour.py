import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

def test_ajouter_pate_panier_carrefour():
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 20)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    hamburger_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".mainbar__nav-toggle-icon")))
    hamburger_button.click()

    slide_epicerie_salee = driver.find_element(By.CSS_SELECTOR, "ul#data-menu-level-0 li[tabindex]:nth-child(12)")
    action.move_to_element(slide_epicerie_salee).perform()

    slide_pate_riz_puree = driver.find_element(By.CSS_SELECTOR, "ul#data-menu-level-1_R12 li:nth-child(7)")
    action.move_to_element(slide_pate_riz_puree).perform()

    slide_pate = driver.find_element(By.CSS_SELECTOR, "ul#data-menu-level-2_R12F05 li:nth-child(3)")
    slide_pate.click()

    openProduct(driver,3)

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    retrait_en_magasin.click()

    input_codepostal = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[class='search-geoloc'] input[data-testid='input-control']")))
    input_codepostal.send_keys("75001")
    sleep(1)
    input_codepostal.send_keys(Keys.ENTER)

    choix_magasin = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "ul.drive-service-list__list li:nth-child(2) button")))
    choix_magasin.click()

    label_disponibilité = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.missing-products__top-title > div")))

    driver.get_screenshot_as_file("screen_disponibilite.png")

    assert label_disponibilité.text == '1 produit indisponible dans ce magasin.'

    driver.quit()

def openProduct(driver,index):
    if index >= 0 and index < 60:
        liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
        liste_produits[index].click()
    else:
        print("Index hors de la range")