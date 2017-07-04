#selenium is a web driver for all browsers that opens the actual browser
#and allows you to automate form actions and clicks and the bypasss of captchas.
#need to import time lib as well as gold finder has a 3 sec delay to prevent me
#from doing this.
from time import sleep
from selenium import webdriver
import os
#the keys object is imported on line 6 to allow automation of 
#a user pressing keys.
from selenium.webdriver.common.keys import Keys

class GetGold():
			
	def searchGold():
		driver = webdriver.Chrome()
		driver.get("https://goldfinder.site")
		but = driver.find_element_by_class_name("g-recaptcha")
		but.send_keys(Keys.RETURN)
		sleep(5)
		input('Fill out captcha and press any key to continue.')
		print(os.getcwd())

if __name__ == "__main__":
	GetGold.searchGold()

#create an instance of webdriver module (bridge from python to browser)
#and specify i'm using its chrome method since thats my browser.
#driver = webdriver.Chrome()

#so far all the program does is launch chrome.
#this next line calls the chrome web driver instance object's "get"
#property to input a URL into the address bar. now when program is ran
#chrome opens https://goldfinder.site/

#driver.get("https://goldfinder.site")

#the site takes around 5 secs to fully load. so we wait.

#but = driver.find_element_by_class_name("g-recaptcha")
#but.send_keys(Keys.RETURN)



#input('Fill out captcha and press any key to continue.')
#print(os.getcwd())