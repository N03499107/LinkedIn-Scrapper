#"Error parsing the JSON: {\"obj.filterParams.searchFilters.memberFilterIds\":[{\"msg\":\"error.path.missing\",\"args\":[]}]}"
#Returns a file containing a list of Linkedin Profiles
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import csv
import io
#start url
url = "https://www.linkedin.com/cap?recruiterEntryPoint=true&trk=nav_account_sub_nav_cap/"

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
)

#browser information
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
#browsers firefox or phantomjs
driver = webdriver.Firefox(executable_path = r"C:\Users\bin\geckodriver.exe")
# driver = webdriver.PhantomJS(executable_path = r"C:\Users\wrafterb1\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin\phantomjs.exe", desired_capabilities = dcap)
driver.set_window_size(1583,834)

#start
driver.get(url)

#login with test account
username = driver.find_element_by_id('session_key-login')
password = driver.find_element_by_id('session_password-login')
username.send_keys('******@gmail.com')
password.send_keys('******')
time.sleep(3)
driver.find_element_by_name('signin').click()
time.sleep(15)



#spoof searching
with io.open('CFO.csv', 'rb') as f:
    reader = csv.reader(f)
    lists = [x[0] for x in csv.reader(f)]
    #print lists
    count = 0
    for i in range(len(lists)):
        try:
            driver.find_element_by_class_name('uncollapse-trigger').click()
            search = driver.find_element_by_class_name('tt-input')
            print lists[i]
            
            search.send_keys(lists[i])
            driver.find_element_by_class_name('submit-button').click()
            time.sleep(10)
            print(driver.current_url)
            link = driver.find_element_by_xpath("//h3[@class='name']/a[1]")
            with open("profiles_sorted_cfo", "a+") as myfile:
                myfile.seek(0,2)
                myfile.write(link.get_attribute('href')+'\n')
        except NoSuchElementException:
            print 'Exception Occurs'

myfile.close()


driver.close()
driver.quit()
