import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class AmazonTest (unittest.TestCase):

    def setUp(self):
        app = ('/Users/anna.belova/Downloads/appium-ios-basic-master/amazon.apk')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4729/wd/hub',
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

   
    def testSearchItem (self):
        sleep (5)
        SkipSignIn = self.driver.find_element_by_id("skip_sign_in_button")
        SkipSignIn.click()
        sleep(5)
        SearchField = self.driver.find_element_by_id ("rs_search_src_text")
        SearchField.click()
        sleep(2)
        SearchField = self.driver.find_element_by_id ("rs_search_src_text")
        #SearchField.send_keys("dress")
        SearchField.send_keys("dress")
        #self.driver.sendKeyEvent(AndroidKeyCode.GO)
        sleep (2)
        self.driver.press_keycode (66)
        sleep(5)
        self.assertIsNotNone(self.driver.find_element_by_class_name('android.webkit.WebView'))



        



