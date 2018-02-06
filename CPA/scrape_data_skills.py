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
outfile = io.open('linkedin_output_skills.csv','ab')
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
            
        ######SKILLS
        try:
            skill = driver.find_elements_by_xpath('//div[@id="profile-skills"]/div[2]/ul/li')
            for skl in skill:
                output.append(skl.text.encode('ascii','ignore'))
        except NoSuchElementException:
            print('No SKILLS') 
      
        worksheet.writerow(output)

driver.close()
driver.quit()
