## Requests Wrapper for Blurr.app ##
##								  ##
##            Ede0m      		  ##


from selenium import webdriver
# from pyvirtualdisplay import Display
import requests
# import webbrowser
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


	def __domainRequest(self, driver):
		
		try:
			r = requests.get(self.domain, timeout=6.0, headers={'user-agent': self.UAs['ChromeMac']})
			self.html = r.text
			driver.get(self.domain)
			# webbrowser.open(self.domain, new = 0)
			# webbrowser.get('/usr/bin/google-chrome %s').open(self.domain, new=0)
		except:
			return
		
		print("\n Visited ", self.domain, '\n')
		time.sleep(self.waitTime)
		


	def __linkRequests(self, driver):
		
		#### THIS method COULD ALSO ADD TO INDEX.JSON WITH ALL THE LINKS IT FINDS? ####

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
					# webbrowser.open(link, new = 0)
					# webbrowser.get('/usr/bin/google-chrome %s').open(link, new=0)
					# r = requests.get(link, timeout=6.0, headers = {'user-agent': self.UAs['ChromeMac']})
					driver.get(link)
					print("		- Linked to ", link)
				except:
					pass
				time.sleep(self.waitTime)
				count += 1

	def run(self, driver):
		self.__domainRequest(driver)
		self.__linkRequests(driver)
		



#display = Display(visible=0, size=(800, 600))
#display.start()
### BROWSER EMULATION ###
# driver = webdriver.Chrome("")
# driver.get('http://www.junk.com/')
# click functionality (naviagte every site a little bit)
#time.sleep(1) # Let the user actually see something!
#driver.quit()
#display.stop()



