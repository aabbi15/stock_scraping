from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import json

with open('NIFTY50.json', 'r') as openfile:
    NIFTY50 = json.load(openfile)


data=[]




driver_path = "C:/Users/abhis/OneDrive/Desktop/stock_scraping/chromedriver-win64/chromedriver.exe"
options = Options()
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')

options.add_argument('--log-level=3')
options.page_load_strategy = 'eager'


driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(5)

i=0;
for company in NIFTY50:

    driver.get(company['link'])
    name_xpath = '//*[@id="stockName"]/h1'
    name = driver.find_element(By.XPATH, name_xpath).text

    company_obj = {
        "name" : name
    }


    # price_xpath = '//*[@id="nsecp"]'
    
    # price_element = driver.find_element(By.XPATH, price_xpath)
    # price = price_element.get_attribute('data-numberanimate-value')

   

    # day_low = driver.find_element(By.ID,'sp_low').text
    # day_high = driver.find_element(By.ID,'sp_high').text

    # yearly_low = driver.find_element(By.ID,'sp_yearlylow').text
    # yearly_high = driver.find_element(By.ID,'sp_yearlyhigh').text

    table_xpath = '//*[@id="stk_overview"]/div[1]/div[1]/div[1]/table/tbody'

    table124 = driver.find_elements(By.CLASS_NAME, 'oview_table')
    # table3 = driver.find_element(By.CLASS_NAME, 'oview_table withspan')

    # tables = table124+table3

    for table in table124 :
        rows = table.find_elements(By.TAG_NAME,'tr')

        for row in rows:
            cols = row.find_elements(By.TAG_NAME,'td')
            
            try:
                
                company_obj[cols[0].text] = cols[1].text
            except:
                print("NO")
            
    data.append(company_obj)

    json_data = json.dumps(data,indent=4)
    print(i)
    i+=1


driver.quit()

with open('maindata.py','w') as outfile:
    outfile.write(json_data)
