##  Main frame for Fluff.app  ##
##
## 		 Garritt Moede 		 ##


import random
import json
from req import Req

print('\n  Loading Index ... \n')
data = None
with open('index.json') as json_data:
    data = json.load(json_data)

print('- Beginning Default Masking - \n')

while True:
	for tag in data.keys():
		for option in data[tag].keys():
			num_entries = data[tag][option]['num']
			if num_entries is 0:
				continue
			key = random.randint(1, num_entries)
			domain = data[tag][option][str(key)]
			r = Req(domain, 3, 5)
			r.run()



