from selenium.webdriver import Chrome
from time import sleep
import math
import os
driver = Chrome()

try:
    driver.get("http://suninjuly.github.io/file_input.html")

    fild1 = driver.find_element_by_name("firstname")
    fild1.send_keys("Danil")
    fild2 = driver.find_element_by_name("lastname")
    fild2.send_keys("Svyatov")
    fild3 = driver.find_element_by_name("email")
    fild3.send_keys("ddsvyatov@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'rer.txt')
    file_button = driver.find_element_by_name("file")
    file_button.send_keys(file_path)

    button = driver.find_element_by_tag_name("button")
    button.click()


finally:
    sleep(2)
