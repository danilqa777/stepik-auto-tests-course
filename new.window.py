from selenium.webdriver import Chrome
from time import sleep
import math
import os
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
driver = Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

button1 = driver.find_element_by_tag_name("button")
button1.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

fild = driver.find_element_by_id("answer")
fild.send_keys(y)

button = driver.find_element_by_tag_name("button")
button.click()