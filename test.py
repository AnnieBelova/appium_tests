import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class LoginTests(unittest.TestCase):

    def setUp(self):
        app = ('/Users/anna.belova/Downloads/appium-ios-basic-master/starter/build/Release-iphonesimulator/AppiumTest.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '13.3',
                'deviceName': 'iPhone 11 Pro Max'
            }
        )
    
    def tearDown(self):
        self.driver.quit()
    
    def testEmailField(self):
        emailTF = self.driver.find_element_by_accessibility_id('EmailTextField')
        emailTF.send_keys("test@appcoda.com")
        emailTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.get_attribute("value"), "test@appcoda.com")

    def testPasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('PasswordTextField')
        passwordTF.send_keys("password")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(len(passwordTF.get_attribute("value")), len("password"))

    def testLoginButton(self):
        self.testEmailField()
        self.testPasswordField()
        loginTF = self.driver.find_element_by_accessibility_id('LoginButton') 
        loginTF.click()
        sleep(1)
        self.assertIsNotNone(self.driver.find_element_by_accessibility_id('Smiley'))



    