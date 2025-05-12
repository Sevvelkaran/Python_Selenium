from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 



driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
wait = WebDriverWait(driver, 10)
btn1 = wait.until(expected_conditions.element_to_be_clickable((By.ID, "btn1")))
btn1.click()
ip1 = wait.until(expected_conditions.visibility_of_element_located((By.ID, "txt1")))
ip1.send_keys("Hello")

btn2 = driver.find_element(By.ID, "btn2")
btn2.click()

wait = WebDriverWait(driver, 10)
ip2 = wait.until(expected_conditions.visibility_of_element_located((By.ID, "txt2")))
ip2.send_keys("World")


