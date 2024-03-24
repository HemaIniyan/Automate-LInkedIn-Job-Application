from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

URL ="https://www.linkedin.com/jobs/search/?currentJobId=3720762386&f_AL=true&f_C=246085&f_E=2&geoId=101165590&keywords=graduate%20software%20engineer&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_btn = driver.find_element(By.CLASS_NAME, value="btn-secondary-emphasis")
sign_in_btn.click()

# Entering sign in details
time.sleep(2)
username_text = driver.find_element(By.ID, value="username")
username_text.send_keys("hemainika2651@gmail.com")
password = driver.find_element(By.ID, value="password")
password.send_keys("Inika@2651")
user_sign_btn = driver.find_element(By.CLASS_NAME, value="from__button--floating")
user_sign_btn.click()

# input("press ENTER after entering the captcha")
time.sleep(45)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable a")

# Apply for Jobs
for listing in all_listings[0:4]:
    print(listing.text)
    listing.click()
    time.sleep(3)
    try:
        easy_link_btn = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        easy_link_btn.click()

        time.sleep(2)
        first_next = driver.find_element(By.CSS_SELECTOR, value=".display-flex button")
        first_next.click()

        time.sleep(3)
        review_btn = driver.find_elements(By.CSS_SELECTOR, value=".display-flex button")
        review_btn[2].click()

        time.sleep(3)
        submit_btn = driver.find_elements(By.CSS_SELECTOR, value=".display-flex button")
        submit_btn[3].click()
        print("Application Submitted successfully")

    except NoSuchElementException:
        print("No easy apply option.")

    except ElementNotInteractableException:
        abort_application()
        print("Complex steps to fill the application.")

driver.quit()
