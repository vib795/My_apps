# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:40:01 2020

@author: utkar
"""
######################################################################
#you need selenium in your environment to run this.                  # 
#before anything open anaconda environments and install selenium and # 
#all the other dependecies anaconda shows you.                       #
#you are good to go after that with this code.                       #
######################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        
    def like_insta(self, hashtag):
        #count = 0 
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        bot.find_element_by_class_name("eLAPa").click()
        for i in range(1,5):
            #bot.find_element_by_class_name('_8-yf5 ').click()
            bot.find_element_by_class_name("wpO6b ").click()
            bot.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            time.sleep(3)
        #bot.find_element_by_class_name("_8-yf5 ").click()
        #time.sleep(5)
        #bot.find_element_by_class_name("glyphsSpriteSettings__outline__24__grey_9 u-__7").click()
        bot.close()
        
ed = InstagramBot('journeyofacamera', 'Yamunawest_05')
ed.login()
ed.like_insta('nature')