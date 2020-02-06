# Visual_Search test for Android device

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

    def testVisualSearch (self):
        sleep (2)
        SkipSignIn = self.driver.find_element_by_id("skip_sign_in_button")
        SkipSignIn.click()
        sleep(2)
        SearchField = self.driver.find_element_by_id ("rs_search_src_text")
        SearchField.click()
        sleep(2)
        CamSearch = self.driver.find_element_by_id ("search_right_cam_img")
        CamSearch.click()
        sleep(2)
        UploadPhoto = self.driver.find_element_by_id("home_page_banner_upload_photo_button")
        UploadPhoto.click()
        sleep(2)
        
        Banner = self.driver.find_element_by_id("allow_camera_access")
        if Banner:
            Banner.click()
            sleep(2)
        
        Allow=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        if Allow:    
            Allow.click()

        sleep(3)
        #UploadImage = self.driver.find_elements_by_id("android:id/title")[1]
        #UploadImage.click()
       # sleep(3)
       
        ChoosePicture = self.driver.find_element_by_xpath("//android.widget.TextView[@text='20200128_064941.jpg']")
        ChoosePicture.click()
        sleep(20)
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='Styles by']"))



        
        
        


          
        







       
        