from selenium.webdriver import Chrome
from time import sleep
import math
import os
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
driver = Chrome()

driver.get("http://suninjuly.github.io/alert_accept.html")

button1 = driver.find_element_by_tag_name("button")
button1.click()
alert = driver.switch_to.alert
alert.accept()

x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = driver.find_element_by_id("answer")
input.send_keys(y)

button = driver.find_element_by_tag_name("button")
button.click()




