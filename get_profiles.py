
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

# Load environment variables from .env file
load_dotenv()

# Open Chrome window in debugging mode via terminal
# Mac -> command to run in terminal before running the .py
# /Applications/Google\ Chrome\ Beta.app/Contents/MacOS/Google\ Chrome\ Beta --remote-debugging-port=9222

USERNAME=os.getenv("NAME")
PASSWORD=os.getenv("PASSWORD")
MAX_RETRIES = os.getenv("MAX_RETRIES")
RETRY_DELAY = os.getenv("RETRY_DELAY") 

# Initialize the WebDriver
def initialize_driver():
    c_options = webdriver.ChromeOptions()
    # c_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    c_options.binary_location = os.getenv("CHROME_LOCATION")  # Replace with the exact path from step 2
    service = Service(os.getenv("DRIVER_LOCATION"))  # Specify the path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=c_options)
    return driver


def make_noise():
    '''Make noise after finishing executing a code'''
    duration = 1  # seconds
    freq = 440  # Hz
    subprocess.call(['play', '-nq', 'synth', str(duration), 'sine', str(freq)])

def get_profiles(driver, url, start_index, end_index, all_profile_links):
    driver.get(url)
    time.sleep(random.randint(2, 10))
    
    profile_list = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.entity-result__title-line.entity-result__title-line--2-lines'))
    )
    for profile in profile_list[start_index:end_index]:
        element = profile.find_element(By.CLASS_NAME, "app-aware-link")
        link = element.get_attribute("href")
        all_profile_links.append(link)

    time.sleep(random.randint(4, 12))
    driver.execute_script(f"window.scrollTo(0, {random.randint(800, 1000)})")

    time.sleep(random.randint(5, 15))

    driver.execute_script("window.scrollTo(0, 0)")
    print("Connecttttttt")
    print(all_profile_links)

      
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



def main():
    try: 
        driver = initialize_driver()
        login(driver, USERNAME, PASSWORD)
        # Open the file for reading
        with open(os.getenv("COMPANY_FILE"), 'r') as file:
            # Read all lines from the file and store them in an array
            elements = file.readlines()

        # Strip newline characters from each element
            
        all_company = [element.strip() for element in elements]
        print(all_company)

        all_search_urls=[]

        for company in all_company:
            current_url1=f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords={company}&origin=FACETED_SEARCH&sid=%2CeI"
            # current_url2=f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords={company}&origin=FACETED_SEARCH&page=2&sid=%2CeI"
            
            all_search_urls.append(current_url1)
            # all_search_urls.append(current_url2)


        # url="https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=Doordash&origin=FACETED_SEARCH&page=2&sid=Isi"
        # "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=Moveworks&origin=FACETED_SEARCH&sid=%2CeI"
        # "https://www.linkedin.com/search/results/people/?keywords=Moveworks&origin=SWITCH_SEARCH_VERTICAL&sid=Q2i"
        all_profile_links = []
        for url in all_search_urls:
            start = 0
            end = 5 #end index is EXCLUSIVE 
            get_profiles(driver, url, start, end, all_profile_links)
            

        # get_profiles(driver, "https://www.linkedin.com/search/results/people/?activelyHiring=%22true%22&geoUrn=%5B%22103644278%22%5D&keywords=Reckitt&origin=FACETED_SEARCH", retries, 0, 5)

        # Write the link to the file
        with open(os.getenv("PROFILE_LINK"), "w") as f:
            # Assuming 'all' is a list of links (strings)
            for profile_link in all_profile_links:
                f.write(profile_link + "\n")  # Add newline character after each link

        # # Write the link to the file
        # with open("sent_company.txt", "a") as f:
        #     # Assuming 'all' is a list of links (strings)
        #     for company in all_company:
        #         f.write(company + "\n")

        # # Open the file for reading
        # with open(os.getenv("USERNAME"), 'w') as file:
        #     # Read all lines from the file and store them in an array
        #     file.write("")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Clean up resources
        driver.quit()
        make_noise()

if __name__ == "__main__":
    main()
    
    

