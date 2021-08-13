import math
import time
import os
import time
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

capabilities = {
    "browserVersion": "92.0",
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False,
    }
}

driver: WebDriver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    print("start!")
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100"))

    driver.find_element_by_id("book").click()
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_id("solve").click()

    print(driver.switch_to.alert.text)


finally:
    driver.quit()

# #Переход на новую вклвдку и работа с ней
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     print("start!")
#     driver.get("http://suninjuly.github.io/redirect_accept.html")
#     time.sleep(5)
#     driver.find_element_by_class_name("trollface").click()
#
# #Переходим на новую вкладку
#     driver.switch_to.window(driver.window_handles[1])
#
#     x = driver.find_element_by_id("input_value").text
#     y = calc(x)
#     print(y)
#     driver.find_element_by_id("answer").send_keys(y)
#     driver.find_element_by_class_name("btn").click()
#     print(driver.switch_to.alert.text)

# finally:
#     time.sleep(10)
#     driver.quit()

# Работа с аллертами
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     driver.get("http://suninjuly.github.io/alert_accept.html")
#
#     driver.find_element_by_class_name("btn").click()
#     driver.switch_to.alert.accept()
#     x = driver.find_element_by_id("input_value").text
#     y = calc(x)
#     driver.find_element_by_id("answer").send_keys(y)
#     driver.find_element_by_class_name("btn-primary").click()
#     print(driver.switch_to.alert.text)
#
# finally:
#     time.sleep(10)
#     driver.quit()


# Урок загрузка файла
#     input1 = driver.find_element_by_name("firstname")
#     input1.send_keys("Ivan")
#     input2 = driver.find_element_by_name("lastname")
#     input2.send_keys("Petrov")
#     input3 = driver.find_element_by_name("email")
#     input3.send_keys("Test@test.ru")
#
#     current_dir = os.getcwd()
#     print(current_dir)
#     file_name = "test.txt"
#     file_path = os.path.join(current_dir, file_name)
#     print(file_path)
#     element = driver.find_element_by_id("file")
#     element.send_keys(file_path)
#     driver.find_element_by_class_name("btn").click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

# Шаг 7
# def calc(x):
#      return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     url = "http://suninjuly.github.io/execute_script.html"
#     driver.get(url)
#
#     v_aluex = driver.find_element_by_id("input_value").text
#     print(v_aluex)
#     x = v_aluex
#     y = calc(x)
#     print(y)
#     button = driver.find_element_by_class_name("btn")
#     answer_input = driver.find_element_by_id("answer")
#     answer_input.send_keys(y)
#     driver.execute_script('return arguments[0].scrollIntoView(true);', button)
#     driver.find_element_by_id("robotCheckbox").click()
#     driver.find_element_by_id("robotsRule").click()
#     button.click()
#     time.sleep(5)

#   Принт текста алерта
#     print(driver.switch_to.alert.text)

#  finally:
#     time.sleep(10)
#     driver.quit()


#     answer = driver.find_element_by_id("answer")
#     answer.send_keys(y)
#     checkbox = driver.find_element_by_id("robotCheckbox")
#     checkbox.click()
# #     radiobutton = driver.find_element_by_id("robotsRule")
#     radiobutton.click()
#     button = driver.find_element_by_class_name("btn-default")
#     button.click()
# finally:
# time.sleep(20)
# driver.quit()


# java script scroll

# button = driver.find_element_by_tag_name("button")
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()


# Select
# figure1 = driver.find_element_by_id("num1")
# figure2 = driver.find_element_by_id("num2")
# figure3 = int(figure1.text) + int(figure2.text)
# print(figure3)
# select = Select(driver.find_element_by_id("dropdown"))
# select.select_by_value(str(figure3))
# driver.find_element_by_class_name("btn").click()


# def calc(x):
#      return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     url = "http://suninjuly.github.io/selects1.html"
#     driver.get(url)
#     x_element = driver.find_element_by_id("treasure")
#     v_aluex = x_element.get_attribute("valuex")
#     print("value of people radio: ", v_aluex)
#     x = v_aluex
#     y = calc(x)
#     answer = driver.find_element_by_id("answer")
#     answer.send_keys(y)
#     checkbox = driver.find_element_by_id("robotCheckbox")
#     checkbox.click()
#     radiobutton = driver.find_element_by_id("robotsRule")
#     radiobutton.click()
#     button = driver.find_element_by_class_name("btn-default")
#     button.click()

# finally:
