import pytest
from datetime import time
import time
from appium import webdriver
import Constant_All as c
import pytest
from appium.webdriver.common.touch_action import TouchAction

@pytest.fixture()
def amazon_dc():

    desired_cap = {"deviceName": "63a06a98",
      "platformName": "Android",
      "app": "C:\\Users\\riddh\\Downloads\\com-amazon-mshop-android-shopping-1241198011-56223854-08e0a550f923f85e5058c089f17e2256.apk",
      "appPackage": "com.amazon.mShop.android.shopping",
      "appWaitActivity": "com.amazon.mShop.home.web.MShopWebGatewayMigrationActivity",
    "automationName": "Uiautomator2"
                   }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    return driver

@pytest.fixture()
def filpkart_dc():
    desired_cap = {"deviceName": "63a06a98",
                   "platformName": "Android",
                   "app": "C:\\Users\\riddh\\Downloads\\flipkart_v7-17.apk",
                   "appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
                   "appPackage": "com.flipkart.android",
                   "automationName": "Uiautomator2"
                   }

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    driver.implicitly_wait(30)
    return driver

@pytest.fixture()
def Mobilesettng_dc():
    desired_cap = {"deviceName": "63a06a98",
                       "platformName": "Android",
                       "appWaitActivity": "com.android.settings.MainSettings",
                       "appPackage": "com.android.settings",
                       "app": "C:\\Users\\riddh\\Downloads\\Settings_9.apk"
                  }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    return driver

