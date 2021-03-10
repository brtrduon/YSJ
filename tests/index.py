from selenium import webdriver
import time

class Ysj_test():
  def __init__(self):
    self.baseUrl = "http://localhost:8002/"
    self.driver = webdriver.Chrome()

    self.driver.maximize_window()
    self.driver.get(self.baseUrl)
    self.driver.implicitly_wait(5)

  def navigation_test(self):
    navigation_list = ["Home", "Menu", "Location"]

    for item in navigation_list:
      link = self.driver.find_element_by_link_text(item)
      link.click()
      time.sleep(2)

    about = self.driver.find_element_by_id("about")
    about.click()
    time.sleep(2)

  def menu_test(self):
    menu_list = ["beef", "chicken", "pork", "goat", "seafood", "dairy", "vegetarian", "rice", "noodle", "all"]

    menu = self.driver.find_element_by_link_text("Menu")
    menu.click()
    time.sleep(2)

    for item in menu_list:
      link = self.driver.find_element_by_id(item)
      link.click()
      time.sleep(2)

  def close(self):
    self.driver.close()

ff = Ysj_test()
ff.navigation_test()
ff.menu_test()
ff.close()