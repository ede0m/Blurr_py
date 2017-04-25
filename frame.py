##  Main frame for blurr.app  ##
##
## 		   ede0m 		      ##
 


#### TODO ####
# 
# - selenium doesn't use correct browsing history
# - Get current users UserAgent, remove hardcoding fool
# 
# - limit to update tab using webrowser module in req.py
# - input settings
#
#


import random
import json
# import webbrowser
from req import Req
from selenium import webdriver
import os

print('\n  Loading Index ... \n')
data = None
with open('index.json') as json_data:
    data = json.load(json_data)

print('- Beginning Default Masking - \n')
# webbrowser.get('/usr/bin/google-chrome %s').open('http://google.com')

path = os.getcwd() + "/chromedriver" # CHANGE CHROMEDRIVE PATH HERE IF USING OS BESIDES MAC OSX
#print(path)
driver = webdriver.Chrome(path)
while True:
	for tag in data.keys():
		## Settings clause somehere around here
		for option in data[tag].keys():
			num_entries = data[tag][option]['num']
			if num_entries is 0:
				continue
			key = random.randint(1, num_entries)
			domain = data[tag][option][str(key)]
			r = Req(domain, 3, 5)
			r.run(driver)



