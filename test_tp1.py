import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    #barre_recherche = driver.find_element(By.ID,"twotabsearchtextbox")
    barre_recherche = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5"+ Keys.ENTER)
    driver.quit()

def test_ajouter_produit_panier_xpath_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    accept_cookies = driver.find_element(By.XPATH, "//input[@class='a-button-input celwidget']")
    accept_cookies.click()
    barre_recherche = driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'][@autocomplete='off']")
    barre_recherche.send_keys("Playstation 5")
    button_recherche = driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'][@value='Go']")
    button_recherche.click()
    premier_produit = driver.find_element(By.XPATH, "//span[ @class ='a-size-base-plus a-color-base a-text-normal']")
    premier_produit.click()
    ajouter_au_panier = driver.find_element(By.XPATH, "//input[@type='button'][@value='Ajouter au panier']")
    ajouter_au_panier.click()
    #non_assurance = driver.find_element(By.XPATH, "//input[@class='a-button-input'][@aria-labelledby='attachSiNoCoverage-announce']")
    #non_assurance.click()
    driver.quit()

def test_ajouter_produit_panier_xpath_carrefour():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    driver.implicitly_wait(2)
    accept_cookies = driver.find_element(By.XPATH, "//div[@class='banner-actions-container']/button")
    accept_cookies.click()
    barre_recherche = driver.find_element(By.XPATH,"//input[@aria-label='Rechercher parmi le contenu du site']")
    barre_recherche.send_keys("1664")
    button_recherche = driver.find_element(By.XPATH,"//button[@aria-label='Rechercher parmi le contenu du site']")
    button_recherche.click()
    premier_produit = driver.find_element(By.XPATH, "//div[@class='main-vertical--image']/a[@href='/p/biere-lager-blonde-sans-alcool-1664-3080216055442']")
    premier_produit.click()
    ajouter_au_panier = driver.find_element(By.XPATH, "//button[@aria-label='ACHETER']")
    ajouter_au_panier.click()
    retrait = driver.find_element(By.XPATH,"//div[contains(@class,'push-services--pickers')]/ul/li[1]")
    livraison = driver.find_element(By.XPATH, "//div[contains(@class,'push-services--pickers')]/ul/li[2]")
    livraison_1h = driver.find_element(By.XPATH, "//div[contains(@class,'push-services--pickers')]/ul/li[3]")
    assert retrait.text == 'Drive\nRetrait gratuit en magasin'
    assert livraison.text == 'Livraison\nVotre plein de course en 24h'
    assert livraison_1h.text == "Livraison 1h\nVos courses d’appoint en 1h"
    driver.quit()


def test_ajouter_produit_panier_css_carrefour():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.screenshot("premier_result.png")
    first_result.click()

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    driver.get_screenshot_as_file("screen_all_option.png")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()

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
    assert label_disponibilité.text == '1 produit indisponible dans ce magasin.'

    driver.quit()

def openProduct(driver,index):
    liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
    liste_produits[index].click()