## Requests Wrapper for Fluff.app ##
##								  ##
##        Garritt Moede			  ##


#from selenium import webdriver
#from pyvirtualdisplay import Display
import requests
import time
import random
from bs4 import BeautifulSoup

class Req (object):

	def __init__(self, domain, nlinks, waitTime):
		self.domain = domain
		self.nlinks = nlinks
		self.waitTime = waitTime
		self.html = None
		self.links = {}
		self.UAs = {
						'ChromeMac':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
						'ChomeWin7':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
						'ChromeLinux':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19'
					}


	def __domainRequest(self):
		try:
			r = requests.get(self.domain, timeout=6.0, headers={'user-agent': self.UAs['ChromeMac']})
			self.html = r.text
		except:
			#print(self.domain)
			return
		
		print("\n Visited ", self.domain, '\n')
		time.sleep(self.waitTime)
		


	def __linkRequests(self):
		
			## extract links ##
		if self.html != None:	
			soup = BeautifulSoup(self.html, 'lxml')
			count = 1
			for link in soup.findAll('a'):
				link = link.get('href')
				if link != None and link.startswith("http"):
					self.links[count] = link
					count += 1
			num_links_found = count
			## follow some links
			count = 0
			while count < self.nlinks:
				key = random.randint(1, num_links_found)
				try:
					link = self.links[key]
					r = requests.get(link, timeout=6.0, headers = {'user-agent': self.UAs['ChromeMac']})
					print("		- Linked to ", link)
				except:
					pass
				time.sleep(self.waitTime)
				count += 1

	def run(self):
		self.__domainRequest()
		self.__linkRequests()
		

#### THIS CLASS COULD ALSO ADD TO INDEX.JSON WITH ALL THE LINKS IT FINDS? ####


#display = Display(visible=0, size=(800, 600))
#display.start()
### BROWSER EMULATION ###
#driver = webdriver.Chrome("/Users/garritt/CODEDOG/DS/noiz/chromedriver")
#driver.get('http://www.junk.com/');
# click functionality (naviagte every site a little bit)
#time.sleep(1) # Let the user actually see something!
#driver.quit()
#display.stop()



