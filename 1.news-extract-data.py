from selenium import webdriver
import pandas as pd
import os
from datetime import datetime
import sys

url = 'https://www.thesun.co.uk/sport/football/' # URL to scrape
path = os.path.expanduser("~") # Path to the ChromeDriver executable

# Creating the driver
service = webdriver.ChromeService()

# Setting the options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") # Run the browser in headless mode

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

# Finding Elements
results = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]/a')

titles = []
subtitles = []
links = []

# Extracting data from the elements
for result in results:
    #print(result.get_attribute("innerHTML"))

   title = result.find_element(by='xpath', value='./span').get_attribute('innerHTML')
   subtitle = result.find_element(by='xpath', value='./h3').get_attribute('innerHTML')
   link = result.get_attribute('href')
   titles.append(title)
   subtitles.append(subtitle)
   links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links} # Create a dictionary with the data
df_headlines = pd.DataFrame(my_dict) # Create a DataFrame from the dictionary
df_headlines.to_csv('headline.csv', sep=';') # Export the DataFrame to a CSV file with a separator ';'

driver.quit()   # Close the browser
