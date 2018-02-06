#Goes to all profiles within list and collects their data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import csv
import io

url = "https://www.linkedin.com/cap?recruiterEntryPoint=true&trk=nav_account_sub_nav_cap/"

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
)

#browser information
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
driver = webdriver.Firefox(executable_path = r"C:\Users\bin\geckodriver-v0.19.0-win64\geckodriver.exe")
#driver = webdriver.PhantomJS(executable_path = r"C:\Users\wrafterb1\AppData\Roaming\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin\phantomjs.exe", desired_capabilities = dcap)
driver.set_window_size(1583,834)


#start
driver.get(url)

# login
username = driver.find_element_by_id('session_key-login')
password = driver.find_element_by_id('session_password-login')
username.send_keys('*******@gmail.com')
password.send_keys('*******')
time.sleep(3)
driver.find_element_by_name('signin').click()
time.sleep(15)



#csv file
outfile = io.open('linkedin_output.csv','ab')
worksheet = csv.writer(outfile)

# loop through profiles from list
with open('profiles_sorted') as f:

    for line in f:   

        output=[]
        url = line
        driver.get(url)
        time.sleep(10)
        print(driver.current_url)
        #scroll down to load everything
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        ######HEADER
        ##name
        try:
            #name = driver.find_element_by_class_name('location-industry').text
            name = driver.find_element_by_xpath('//div[@class="profile-info"]/h1').text
        except NoSuchElementException:
            name = '0'
        output.append(name.encode('ascii','ignore'))
        ##Position
        try:
            headerPosition = driver.find_element_by_xpath('//div[@class="profile-info"]/ul/li[1]').text
        except NoSuchElementException:
            print('Error')
        output.append(headerPosition.encode('ascii','ignore'))
        ##Location
        try:
            headerLocation = driver.find_element_by_xpath('//li[@class="location-industry"]/span').text
        except NoSuchElementException:
            print('Error')
        output.append(headerLocation.encode('ascii','ignore'))

        ######EXPERIENCE
        try:
            experience = driver.find_elements_by_xpath('//div[@id="profile-experience"]/div[2]/ul/li/div')
            for school in experience:
                try:
                    pos = school.find_element_by_tag_name('h4').text
                    output.append(pos.encode('ascii','ignore'))
                    at = school.find_element_by_tag_name('h5').text
                    output.append(at.encode('ascii','ignore'))
                    yr = school.find_element_by_tag_name('p').text
                    output.append(yr.encode('ascii','ignore'))
                    dur = school.find_element_by_class_name('duration').text
                    output.append(dur.encode('ascii','ignore'))
                    #loc = school.find_element_by_class_name('location').text
                    #output.append(loc.encode('ascii','ignore'))
                except NoSuchElementException:
                    output.append(0)                
        except NoSuchElementException:
            print('No EXPERIENCE')

        worksheet.writerow(output)

driver.close()
driver.quit()
