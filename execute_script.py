from selenium.webdriver import Chrome
from time import sleep
import math
driver = Chrome()
def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

driver.get("http://SunInJuly.github.io/execute_script.html")

x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

fild_scroll = driver.find_element_by_id("answer")
driver.execute_script("return arguments[0].scrollIntoView(true);", fild_scroll)

fild = driver.find_element_by_id("answer")
fild.send_keys(y)

option1 = driver.find_element_by_id("robotCheckbox")
option1.click()

option2 = driver.find_element_by_id("robotsRule")
option2.click()

button = driver.find_element_by_tag_name("button")
button.click()



