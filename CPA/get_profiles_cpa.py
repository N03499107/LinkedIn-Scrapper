#Returns a file containing a list of Linkedin Profiles
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time
import sys

#start url
url = "https://www.linkedin.com/cap?recruiterEntryPoint=true&trk=nav_account_sub_nav_cap/"

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
)

#browser information
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
#browsers firefox or phantomjs
driver = webdriver.Firefox(executable_path = r"C:\Users\bin\geckodriver-v0.19.0-win64\geckodriver.exe")
# driver = webdriver.PhantomJS(executable_path = r"C:\Users\wrafterb1\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin\phantomjs.exe", desired_capabilities = dcap)
driver.set_window_size(1583,834)

#start
driver.get(url)

#login with test account
username = driver.find_element_by_id('session_key-login')
password = driver.find_element_by_id('session_password-login')
username.send_keys('*******@gmail.com')
password.send_keys('*******')
time.sleep(3)
driver.find_element_by_name('signin').click()
time.sleep(15)



#spoof searching
driver.find_element_by_class_name('uncollapse-trigger').click()
search = driver.find_element_by_id('tt-behavior21')
search.send_keys('cpa')
driver.find_element_by_class_name('submit-button').click()
time.sleep(10)


#go to other search pages, where 100 is the max with free account
    # next page in search
    
for page in range(0,976,25):           
	url = "https://www.linkedin.com/recruiter/smartsearch?searchHistoryId=1879426356&searchCacheKey=f12fe0ba-73d2-49ae-b4fc-39da396706cc%2Cdxpq&searchRequestId=7d3071d7-0a82-4b2c-a765-0ace73345c6d%2CbMGu&searchSessionId=1879426356&linkContext=Controller%3AsmartSearch%2CAction%3Asearch%2CID%3A1879426356&doExplain=false&start=0"	+str(page)	   
	#https://www.linkedin.com/recruiter/smartsearch?searchHistoryId=1879426356&searchCacheKey=f12fe0ba-73d2-49ae-b4fc-39da396706cc%2Cdxpq&searchRequestId=7d3071d7-0a82-4b2c-a765-0ace73345c6d%2CbMGu&searchSessionId=1879426356&linkContext=Controller%3AsmartSearch%2CAction%3Asearch%2CID%3A1879426356&doExplain=false&start=0
	driver.get(url)
	time.sleep(10)

		#scroll to the bottom to load all profiles
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	print(driver.current_url)
	time.sleep(5)
		#store links of profiles in file
	links=[]
	links = driver.find_elements_by_xpath("//h3[@class='name']/a[1][contains(@title,'CPA')]")
	print links
	for i in links:
		print(i.get_attribute('href')) 
		try:
				#if not private profile
			if '#' not in i.get_attribute('href'):
				with open("profiles_sorted", "a+") as myfile:
						# if not already found
					if i.get_attribute('href') not in myfile.read():
							#save profiles URL
						myfile.seek(0,2)
						myfile.write(i.get_attribute('href')+'\n')
		except IndexError:
			print('Index Error, Continuing')

myfile.close()


driver.close()
driver.quit()
