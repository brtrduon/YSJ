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
    home = self.driver.find_element_by_link_text("Home")
    home.click()
    time.sleep(2)

    menu = self.driver.find_element_by_link_text("Menu")
    menu.click()
    time.sleep(2)

    location = self.driver.find_element_by_link_text("Location")
    location.click()
    time.sleep(2)

    about = self.driver.find_element_by_id("about")
    about.click()
    time.sleep(2)

  def close(self):
    self.driver.close()

ff = Ysj_test()
ff.navigation_test()
ff.close()