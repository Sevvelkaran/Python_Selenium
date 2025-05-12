from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests 


def verify_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"{url} - {response.reason}")
        else:
            print(f"{url} - {response.reason} - is broken link")
    except Exception as e:
        print(f"{url} - is broken link ({e})")


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")
links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']/div/ul/li/a")

print(f"Total links found: {len(links)}")

# Check if links are valid
for link in links:
    url = link.get_attribute("href")
    if url:
        verify_url(url)

# Open each link in a new tab
for link in links:
    act = ActionChains(driver)
    act.key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()

driver.quit()
