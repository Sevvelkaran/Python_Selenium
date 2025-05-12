from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")
driver.implicitly_wait(10)

email = driver.find_element(By.NAME, "email")
email.send_keys("2k21cse189@kiot.ac.in")

pwd = driver.find_element(locate_with(By.TAG_NAME, "input").below(email))
pwd.send_keys("Sevvelkaran@0715")

num = driver.find_element(locate_with(By.TAG_NAME, "input").below(pwd))
num.send_keys("9361842608")




wait = WebDriverWait(driver, 10)
box = wait.until(expected_conditions.visibility_of_element_located((By.ID, "signup-termservice")))
box.click()


signup = driver.find_element(locate_with(By.TAG_NAME, "input").below(box))
signup.click()

