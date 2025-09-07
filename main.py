#test the program first, before using in the one you want to buy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

chrome_prefs = {
    "profile.default_content_setting_values": {"images": 2,"popups": 2},
    "profile.managed_default_content_settings": {"images": 2, "stylesheets": 2, "fonts": 2,"media_stream": 2},
}

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'  # Eager load strategy
chrome_options.add_experimental_option("prefs", chrome_prefs)
#chrome_options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=chrome_options)

cookies = [
    #use you own cookies stored in thaiticketmaster.com
]

#link, replace with the show you want to watch
driver.get('https://www.thaiticketmajor.com/concert/taeyang-2025-tour-the-light-year-in-bangkok.html') # change

for cookie in cookies:
    driver.add_cookie(cookie)
    
driver.refresh()

wait = WebDriverWait(driver, timeout=9999)
short_wait = WebDriverWait(driver, 0.5)

#time, set time for it to automatic start

# target_time = "11:59:57"

# while True:
#     current_time = datetime.now().strftime("%H:%M:%S")
#     if current_time >= target_time:
#         break
#     time.sleep(0.5)
# while True:
#     current_time = datetime.now().strftime("%H:%M:%S")
#     if current_time >= "12:00:01":
#         break
#     driver.refresh()
#     time.sleep(1)


#click the time button to go to ticket selection
#replace the data-button by inspect that button
try:
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-button='7682']")))
    driver.execute_script("arguments[0].click();", button)
except Exception as e:
    print(f"An error occurred: {e}")
    

# some has bot check questions
'''
#bot check questions
try:
    driver.find_element(By.XPATH, "//button[contains(@class, 'bg-gradient-to-r')]").click()
except Exception as e:
    print(f"An error occurred: {e}")
#

#solve question

#
try:
    confirm_button = driver.find_element(By.XPATH, "//button[contains(@class, 'bg-blue-600')]").click()
except Exception as e:
    print(f"An error occurred: {e}")
'''

if 'verify_condition' in driver.current_url:
    try:
        element = driver.find_element(By.CSS_SELECTOR, "label[for='rdagree'] strong.label-txt")
        #action = ActionChains(driver)
        #action.move_to_element(element).perform()
        #time.sleep(random.uniform(0.5, 0.75))
        driver.execute_script("arguments[0].click();", element)
        #time.sleep(random.uniform(0.5, 0.75))
        short_wait.until(EC.element_to_be_clickable((By.ID, "btn_verify"))).click()
    except Exception as e:
        print(f"An error occurred: {e}")
        
#zone, replace with the zone you want, seated zone is fixed.php#{zone_number}, standing is festival.php#{zone_number}
try:
    area_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "area[href*='fixed.php#V2']"))) # change
    driver.execute_script("arguments[0].click();", area_element)
except Exception as e:
    print(f"An error occurred: {e}")

#seat, change the number of iteration to the number of ticket you want to buy, maxium for one account is 5
#reselling tickets is illegal
try:
    for i in range(5):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.seatuncheck")))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.seatuncheck")))[i].click()
except Exception as e:
    print(f"An error occurred: {e}")


try:
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[span[text()='Book Now']]"))).click()
except Exception as e:
    print(f"An error occurred: {e}")
input('enter')
