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

driver.get("http://suninjuly.github.io/find_xpath_form")
name = driver.find_element_by_name("first_name")
name.send_keys("Dan")

lastname = driver.find_element_by_name("last_name")
lastname.send_keys("svy")

city = driver.find_element_by_name("firstname")
city.send_keys("mos")

con = driver.find_element_by_id("country")
con.send_keys("rus")

button = driver.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
button.click()