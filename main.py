#from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import datetime

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import csv
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Indeed.com
driver.get("https://in.indeed.com/jobs?q=machine+learning&l=India")

# Optionally, maximize the window
driver.maximize_window()

# Close the browser after some time or interaction
# driver.quit()

#
#css-1qv0295 e37uo190 for company name outside one not in

#class="jcs-JobTitle css-jspxzf eu4oa1w0" of job name  inside one

wait = WebDriverWait(driver, 10)
#job_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-5lfssm eu4oa1w0')))
#job_cards = wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME, "css-5lfssm eu4oa1w0"))
job_cards = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

#for job_card in job_cards:
     # Extract job title
    #job_title = job_card.find_element(By.ID, 'jobTitle-caed92a006476fd8').text
    
    # Extract company name
    #company_name = job_card.find_element(By.CLASS_NAME, 'css-1qv0295 e37uo190').text
try:
    # Wait for the job title element to be present
    job_title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'jobTitle-caed92a006476fd8'))
    )
    # Extract and print the job title text
    job_title = job_title_element.text
    print(job_title)
finally:
    # Close the WebDriver
    driver.quit()


    #print(f"Job Title: {job_title}")
    #print(f"Company Name: {company_name}")
    #print("-" * 40)

driver.quit()





#def main():
 #   driver = webdriver.Chrome()

#    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=India&txtKeywords=&txtLocation=India'

 #   driver.get(url)

#    print(driver.page_source)

    #driver.find('span', id='closeSpanId')
    #driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/table/tbody/tr/td[2]/div/span').click()

    #time.sleep(10)

    #soup= BeautifulSoup(driver.page_source, 'html5lib')
    #print(soup)

#main()