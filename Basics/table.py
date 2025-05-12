from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://thinking-tester-contact-list.herokuapp.com/")

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("kakda@gmail.com")
pwd = driver.find_element(By.XPATH, "//input[@id='password']")
pwd.send_keys("1029384756", Keys.ENTER)

expected_name = "Babu A"
time.sleep(2)
contact_names = driver.find_elements(By.XPATH, "//table[@id='myTable']/tr/td[2]")
contact_count = len(contact_names)
print(contact_count)

for name in contact_names:
    print(name.text)

i = 1
time.sleep(2)
for name in contact_names:
    if name.text == expected_name:
        actual_rowdata = driver.find_element(By.XPATH, f"//table[@id='myTable']/tr[{i}]")
        actnames = actual_rowdata.find_elements(By.TAG_NAME, "td")
        for actname in actnames:
            print(actname.text)
    i += 1

driver.quit()
