# Blurr_py
Tool that camouflages your browsing data with a controlled stream of meaningless web-traffic.

check out the [chrome extension](https://chrome.google.com/webstore/detail/blurr/mmdcjjfkgpccnbcocnfomkldcooghhpp?authuser=1)

**Notes**:
  
  The program can be used with *selenium*, a browser emulator, or pythons *webbrowser* module.
  
  When using with selenium, if you are not running an Apple OS or want to use a browser other than Chrome, you will need to replace the chromedriver file in the repository along with a path varible in frame.py according to your OS's appropriate browser driver.[ More information here](http://www.seleniumhq.org/download/) 
  
  When using the webbrowser module, the program will use your default browser. However note that tab update is currently not functioning.


**Dependencies**: 

- pip3 install selenium
- pip3 install bs4
- pip3 insatll requests 

**Run**:
`python3 frame.py`

