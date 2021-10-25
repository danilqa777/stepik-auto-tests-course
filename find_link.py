from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os


x = str(math.ceil(math.pow(math.pi, math.e)*10000))

driver = Chrome()

driver.get("http://suninjuly.github.io/find_link_text")

num1 = driver.find_element_by_link_text(x)
num1.click()

name = driver.find_element_by_name("first_name")
name.send_keys("Danil")
name2 = driver.find_element_by_name("last_name")
name2.send_keys("Svyatov")
city = driver.find_element_by_name("firstname")
city.send_keys("Moscow")
rus = driver.find_element_by_id("country")
rus.send_keys("Russia")

button = driver.find_element_by_tag_name("button")
button.click()


