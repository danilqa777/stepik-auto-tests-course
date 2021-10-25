from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os

driver = Chrome()
driver.get("http://suninjuly.github.io/registration2.html")

name = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
name.send_keys("Dan")

lastname = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
lastname.send_keys("Svy")

email = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
email.send_keys("@@")

driver.execute_script("window.scrollBy(1000, 10000);")

button = driver.find_element_by_tag_name("button")
button.click()

regist_elt = driver.find_element_by_tag_name("h1")
regist_text = regist_elt.text
assert "Congratulations! You have successfully registered!" == regist_text



