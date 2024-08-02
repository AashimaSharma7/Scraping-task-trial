from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import csv
import re

#setting driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--disable-gpu')

#creating driver
driver = webdriver.Chrome(options=options)

url = "https://in.indeed.com/jobs?q=machine+learning&l=India"
driver.get(url)

wait = WebDriverWait(driver, 5)






positions = []
companies = []
#description = []


# Find job cards

job_cards = driver.find_elements(By.XPATH, "//div[@class='job_seen_beacon']")
for job_card in job_cards:
        #find job position
        try:
            position = job_card.find_element(By.CLASS_NAME,"jobTitle css-198pbd eu4oa1w0").text
            positions.append(position)
        except NoSuchElementException:
            positions.append("no position description")

        #find company
        try:
            company = job_card.find_element(By.CLASS_NAME,"css-63koeb eu4oa1w0").text
            companies.append(company)
        except NoSuchElementException:
            companies.append("no company description")


print("Job Positions and Companies:")
for pos, comp in zip(positions, companies):
    print(f"Position: {pos} - Company: {comp}")
    
    
    
    # #jobTitle-caed92a006476fd8 job position id selector