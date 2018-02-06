# LinkedIn-Scrapper
This Application is used to retrieve all CPA(Certified Public Accountant) and CFO [Chief Financial Officer] information within United States using Python for research purpose.

###For CPA
The project is broken down into multiple python files

### get_profiles.py
This file is the one that retrieves actual profiles from LinkedIn

Utilizing Selenium for many tasks
The first thing is to user agent spoofing and set up the browser
I have either Firefox(gecko) or PhantomJs as the browser, while the other is commented out
PhantomJs is headless so it is faster and runs in the background
But I have gotten better luck using Firefox for the most part, you can also experiment with a virtual desktop to have it out of the way.

Next I log in to my test LinkedIn account, which you can use

Then I do one spoof search, which probably isn't necessary 

LinkedIn Recruiter Lite account provide 40 pages to iterate. Each page has 25 profile's url.
And find the href of each profile located from their profile photo.
If the href is from a private profile it will contain a '#' so I skip it

The output is stored into "profiles_sorted". 

### scrape_data.py
This file actually visits each profile and collects the data
Uses Selenium again

The start of the file is mostly the same as above

Then I loop through that "profiles_sorted" file,
visit each profiles, scroll to load everything and collect all of the data.
I have created scrape_data_Experience.py, scrape_data_Education.py, scrape_data_Certificate.py, scrape_data_skills.py
The reason to make different file is to maintain relationship of columns in csv file.

## Output
	linkedin_output.csv is the actual output produced by scrape_data
	Each scrape_data.py file generate different LinkedIn_Output.csv file 
	Finally I concat all files into LinkedIn_Output.csv file. 

## Helpful URLs
	http://selenium-python.readthedocs.io/
	
