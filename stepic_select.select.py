from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

driver = Chrome()

driver.get("http://suninjuly.github.io/selects1.html")

n1 = driver.find_element_by_id("num1")
n2 = driver.find_element_by_id("num2")

x = n1.text
y = n2.text
s = int(x) + int(y)

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(s))

button = driver.find_element_by_class_name("btn.btn-default")
button.click()


