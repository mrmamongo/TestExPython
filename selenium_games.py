import csv
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import constants


def load_page(drv: webdriver.Chrome) -> bool:
    max_tries = 5
    count_tries = 0
    while count_tries <= max_tries:
        try:
            driver.get('https://www.fonbet.ru/')
            WebDriverWait(drv, constants.delay).until(EC.presence_of_element_located((By.XPATH, constants.check_elem_xpath)))
            driver.find_element(by=By.XPATH, value=constants.search_xpath).click()
            return True
        except TimeoutException:
            count_tries += 1
            return False


values = []
with open(constants.buffer_filename, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        values.append({row['id']: row['gamers']})

game_to_inspect = list(random.choice(values).values())[0]
driver = webdriver.Chrome()

if load_page(driver):
    find = driver.find_element(by=By.XPATH, value=constants.search_panel_xpath)
    find.send_keys(game_to_inspect)
    find.send_keys(Keys.RETURN)
    find = WebDriverWait(driver, constants.delay).until(EC.presence_of_element_located((By.XPATH, constants.found_value_xpath)))
    find.click()
    find = WebDriverWait(driver, constants.delay).until(EC.presence_of_element_located((By.XPATH, constants.game_name_xpath)))
    print(find.text)
else:
    print("Couldn't load page")

driver.close()
driver.quit()
