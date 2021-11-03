
from selenium import webdriver
browser = webdriver.Chrome(executable_path = "C:\SeleniumDrivers\chromedriver.exe")

# start browser session
browser = webdriver.Chrome()

#open codechef in browser
browser.get("https://codechef.com")

#enter username
username = browser.find_element_by_id("edit-name")
username.send_keys("USER NAME")

#pass entry
pasw = browser.find_element_by_id("edit-pass")
pasw.send_keys("PASSWORD")

#submit usrname and pass
browser.find_element_by_id("edit-submit").click()

# open submission page
browser.get("https://www.codechef.com/submit/PROBLEM-NAME")
.
# for poor and slow connection
time.sleep(10)

# open toggle editor
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#upload solution file
with open("solution.cpp.txt",'r') as f:
  code = f.read()

code_element = browser.find_element_by_id('edit-program')
code_element.send_keys(code)

# language option 
browser.find_element_by_xpath('//*[@id="edit-language"]/option[i]')  # replace 'i' with the lagnuage of code you want

#final submission
browser.find_element_by_id("edit-submit").click(
  

