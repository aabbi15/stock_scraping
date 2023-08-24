from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.options import Options

import json






options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('--no-sandbox')
# options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
# options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')

driver = webdriver.Chrome(options=options)



NIFTY50 = []

nifty50_link = 'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9'
driver.get(nifty50_link)

table =driver.find_element(By.XPATH,'//*[@id="mc_mainWrapper"]/div[2]/div[1]/div[5]/div[2]/div/table')
tr = table.find_elements(By.TAG_NAME, "tr")

for row in tr:
    columns = row.find_elements(By.TAG_NAME, 'td')
    
    try:
        name = columns[0].text
        link = columns[0].find_element(By.TAG_NAME,'a').get_attribute('href')

        
        NIFTY50.append({
            "name":name,
            "link":link
            })
    except:
        print("Empty row")

print(NIFTY50)

json_object = json.dumps(NIFTY50, indent=4)
 
# Writing to sample.json
with open("NIFTY50.json", "w") as outfile:
    outfile.write(json_object)