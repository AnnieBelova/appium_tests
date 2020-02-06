       
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class MenuTest(unittest.TestCase):

    def setUp(self):
        app = ('/Users/anna.belova/Downloads/appium-ios-basic-master/amazon_app/amazon.apk')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4724/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': 'heroqlteue',
                'automationName': 'uiautomator2'
            }
        )
    
    def tearDown(self):
        self.driver.quit()   

    
    def testOpenMenu(self):
        sleep (2)
        SkipSignIn = self.driver.find_element_by_id("skip_sign_in_button")
        SkipSignIn.click()
        sleep(3)
        Hamb = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@bounds='[0,72][144,228]']")
        Hamb.click()
        sleep(2)
        Home = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Home']")
        Home.click()
        sleep(3)
        self.assertIsNotNone(self.driver.find_element_by_id('glow_subnav_ingress'))
        sleep(2)