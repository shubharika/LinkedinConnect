from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import random
import time
import os 
import subprocess
from dotenv import load_dotenv

load_dotenv()
# Open Chrome window in debugging mode via terminal
# Mac -> command to run in terminal before running the .py
# /Applications/Google\ Chrome\ Beta.app/Contents/MacOS/Google\ Chrome\ Beta --remote-debugging-port=9222
USERNAME=os.getenv("NAME")
PASSWORD=os.getenv("PASSWORD")
MAX_RETRIES = int(os.getenv("MAX_RETRIES"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY")) # seconds
MESSAGE=os.getenv("MESSAGE")

# Initialize the WebDriver
def initialize_driver():
    c_options = webdriver.ChromeOptions()
    # c_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    c_options.binary_location = os.getenv("CHROME_LOCATION")  # Replace with the exact path from step 2
    service = Service(os.getenv("DRIVER_LOCATION"))  # Specify the path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=c_options)
    return driver

# Process the profile with initial connect button
def process_profile(driver, message):
    print("----------Connectttt-----------------")

    # time.sleep(random.randint(10, 120))
    
    

    # connect_btn = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action'))
    # )

    # connect_btn.click()
    # print("Connecttttttttt")

    time.sleep(random.randint(1, 7))

    add_note_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1'))
    )

    add_note_btn.click()
    print("Addddddddd")

    text_area = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3'))
    )

    text_area.send_keys(message)


    time.sleep(random.randint(18, 47))

    send_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1'))
    )

    send_btn.click()
    print("Senddddddddd")

    time.sleep(random.randint(4, 10))

# Process the profile with secondary connect button
def process_profile_2(driver, message):
    print("------------2nd Connect---------------")

    time.sleep(random.randint(2, 9))

    add_note_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1'))
    )

    add_note_btn.click()
    print("Addddddddd")

    text_area = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3'))
    )

    text_area.send_keys(message)

    time.sleep(random.randint(10, 41))

    send_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1'))
    )

    send_btn.click()
    print("Senddddddddd")
    time.sleep(random.randint(5, 9))

# Process the profile with "More" dropdown
def process_profile_more(driver, message):
    print("-------------Moreeeeee--------------")
    driver.maximize_window()

    time.sleep(random.randint(2,6))

    more_btns = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2'))
    )

    more_btns[1].click()
    print("Moreeeeee")

    time.sleep(random.randint(7, 16))

    connect_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.artdeco-dropdown__item.artdeco-dropdown__item--is-dropdown.ember-view.full-width.display-flex.align-items-center'))
    )

    connect_btn[7].click()
    print("Connecttttttttt")

    time.sleep(random.randint(4, 14))

    add_note_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1'))
    )

    add_note_btn.click()
    print("Addddddddd")

    text_area = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3'))
    )

    text_area.send_keys(message)

    time.sleep(random.randint(14, 39))

    send_btn = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1'))
    )

    send_btn.click()
    print("Senddddddddd")

    time.sleep(random.randint(4, 10))
    print("-------------------")

# Check and process profiles based on the type of button
    
def check_profile(driver, url, retries):
    try: 
        driver.get(url)
        time.sleep(random.randint(2, 10))
        
        text_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.text-heading-xlarge.inline.t-24.v-align-middle.break-words'))
    )
        first_name = text_element.text.split(" ")[0]

        message = f"Hi {first_name}," + MESSAGE
        # message = f"Hi {first_name}"
        button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action")))
        
        new_button_element = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.pvs-profile-actions__action")))
        
        span_element = button_element.find_element(By.CLASS_NAME, "artdeco-button__text")
        span_text = span_element.text
        print("Text inside span:", span_text)

        span_element2 = new_button_element[1].find_element(By.CLASS_NAME, "artdeco-button__text")
        span_text2 = span_element2.text
        print("Text inside 2nd span:", span_text2)

        driver.execute_script(f"window.scrollTo(0, {random.randint(800, 1000)})")

        time.sleep(random.randint(27, 51))

        driver.execute_script("window.scrollTo(0, 0)")

        time.sleep(random.randint(4, 12))

        if span_text == "Connect":
            test.append(url)
            button_element.click()
            process_profile(driver, message)
        elif span_text2 == "Connect":
            time.sleep(random.randint(2, 10)) 
            new_button_element[1].click()
            process_profile_2(driver, message)
        else:
            test2.append(url)
            process_profile_more(driver, message)
    except Exception as e:
                print(f"Error occurred: {e}")
                print(f"Refreshing the page and continuing from {url}")
                if retries < MAX_RETRIES:
                    print(f"Error occurred: {e}")
                    print(f"Retrying ({retries + 1}/{MAX_RETRIES})...")
                    driver.refresh()
                    time.sleep(RETRY_DELAY)
                    check_profile(driver, url, retries=retries + 1)
                else:
                    print("Max retries exceeded. Unable to process profile.")
                    print(f"Error details: {e}")
    finally:
        time.sleep(random.randint(5, 60))
        # Print the lists
        print("Connecttttttt")
        print(test)
        print("Moreeee")
        print(test2)
        
def login(driver, username, password):
    driver.get("https://www.linkedin.com")
    time.sleep(random.randint(2, 4))
    button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis")))
    
    # print(button_element)
    button_element.click()

    username_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "username")))
    time.sleep(random.randint(2, 4))

    username_input.send_keys(username)
    time.sleep(3)
    password_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "password")))
    time.sleep(random.randint(2, 4))

    password_input.send_keys(password)
    
    sign_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")))
    sign_in_button.click()



        
test = []
test2 = []


def make_noise():
    '''Make noise after finishing executing a code'''
    duration = 1  # seconds
    freq = 440  # Hz
    subprocess.call(['play', '-nq', 'synth', str(duration), 'sine', str(freq)])

def main():
    try:
    
        # Open the file for reading
        with open(os.getenv("PROFILE_LINK"), 'r') as file:
            # Read all lines from the file and store them in an array
            elements = file.readlines()

        # Strip newline characters from each element
        allUrl = [element.strip() for element in elements]

        driver = initialize_driver()

        login(driver, USERNAME, PASSWORD)

        
        for url in allUrl:
            check_profile(driver, url, 0)
        
        # Empty the contents of the file after sending request to all 
        with open(os.getenv("PROFILE_LINK"), "w") as f:
            # Content of the file is overwritten with nothing (empty string)
            f.write("")
    
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error, log it, or take appropriate action
        
    finally:
        # Clean up resources
        driver.quit()
        make_noise()

if __name__ == "__main__":
    main()
    
