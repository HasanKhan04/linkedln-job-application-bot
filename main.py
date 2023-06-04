from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)

service = Service(r"C:\Users\hasan\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3451421183&f_AL=true&keywords=software%20developer&refresh=true")

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(1)
email = driver.find_element(By.ID, "username")
email.send_keys("hasanw.khan04@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("gwknass1")
sign_in_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()
time.sleep(1)




all_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in all_jobs:
    job.click()
    easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(1)
    overflow_bar = driver.find_element(By.CLASS_NAME, "overflow-x-hidden")
    scroll_origin = ScrollOrigin.from_element(overflow_bar)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 12000).perform()
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'footer button')
    if submit_btn.get_attribute("aria-label") == "Continue to next step":
        close = driver.find_element(By.CLASS_NAME, "mercado-match")
        close.click()
        discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
        discard.click()
        time.sleep(3)

