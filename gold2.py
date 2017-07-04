from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GetGold():
			
	def searchGold():
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://goldfinder.site")
		sleep(5)
		driver.find_element_by_class_name("g-recaptcha").send_keys(Keys.RETURN)
		input("press a button when finished")		

if __name__ == "__main__":
	GetGold.searchGold()