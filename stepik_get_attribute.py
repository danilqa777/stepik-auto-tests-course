from selenium.webdriver import Chrome
import time
import math

driver = Chrome()

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

driver.get("http://suninjuly.github.io/get_attribute.html")

image = driver.find_element_by_id("treasure")
image_x = image.get_attribute("valuex")

print(image_x)
y = calc(image_x)

search_bar = driver.find_element_by_id("answer")
search_bar.send_keys(y)

option1 = driver.find_element_by_id("robotCheckbox")
option1.click()

option1 = driver.find_element_by_id("robotsRule")
option1.click()

button = driver.find_element_by_class_name("btn.btn-default")
button.click()

