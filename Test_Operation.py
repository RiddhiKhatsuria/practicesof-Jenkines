
from appium.webdriver.common.touch_action import TouchAction
import time
import Constant_All as c

def test_flipkart(filpkart_dc):

    driver = filpkart_dc
    driver.find_element_by_xpath(c.flip_Xpath_English).click()
    driver.find_element_by_id(c.flip_btn1).click()
    driver.find_element_by_id(c.flip_btn2).click()
    driver.find_element_by_id(c.flip_search).click()
    driver.find_element_by_accessibility_id(c.flip_sand).send_keys("Mobile")
    driver.find_element_by_xpath(c.flip_mob).click()
    driver.find_element_by_id(c.flip_btn3).click()
    TouchAction(driver).tap(None, 501, 604, 1).perform()
    time.sleep(3)
    time.sleep(3)
    # It is a Price of POCO M3
    # While I am doing it First mobile is mobile POCO M3
    price = driver.find_element_by_xpath("//android.widget.TextView[@bounds='[44,1426][277,1503]']").get_attribute("text")
    assert price == "₹10,999", "Price does not match Because as of mow poco M3 is not first"


def test_mobile_settings(Mobilesettng_dc):

    driver = Mobilesettng_dc
    TouchAction(driver).tap(None, 413, 1380, 1).perform()
    driver.find_element_by_id(c.setting_id).click()
    time.sleep(3)

def test_amazon(amazon_dc):

    driver = amazon_dc
    driver.find_element_by_id(c.Amazon_btn1).click()
    TouchAction(driver).tap(None, 413, 1380, 1).perform()

