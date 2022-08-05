import datetime
import time

from HomePage import HomePage
from ProductCategoryPage import ProductCategoryPage
from ProductPage import ProductPage
from selenium import webdriver

def test_epiceriesale_pate_buy_drive():
    driver = webdriver.Chrome()
    h = HomePage(driver)
    h.SetupPage()
    h.CloseCookie()
    h.OpenMenu()
    h.OpenCategoryMenu('Epicerie salée')
    h.OpenCategorySubMenu(7)
    h.OpenProductCategoryPage(3)
    pcp = ProductCategoryPage(driver)
    pcp.openProductsPage(3)
    pp = ProductPage(driver)
    pp.Buy()
    pp.ChooseDeliveryMethod(1)
    pp.EnterZipCode("75001")
    pp.SelectStore(2)
    test_availibility = pp.GetAvailabilityStatus()

    assert test_availibility == "1 produit indisponible dans ce magasin."
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    screenshot_name = f'C:\\Users\\ib\\PycharmProjects\\a4q\\screenshots\\capture{date_stamp}.png'
    driver.get_screenshot_as_file(screenshot_name)
    print("Test is PASSED !!!!")
