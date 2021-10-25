from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
button = driver.find_element_by_id("book")
price = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

button.click()
x_element = driver.find_element_by_id("385")
x = x_element.text
y = calc(x)

fild = driver.find_element_by_id("answer")
fild.send_keys(y)

press = driver.find_element_by_id("solve")
press.click()

