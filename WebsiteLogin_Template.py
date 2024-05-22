import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "Enter Your Username/Email"
password = "Enter Your Password"

# Specify the path to the chromedriver
driver = webdriver.Chrome()

# Open Google
driver.get('https://admin.b360.autodesk.com/login')
driver.maximize_window()

# Wait for the page to load completely
time.sleep(2)  # Adjust the sleep time if necessary

# Find the search box element using its name attribute
driver.find_element(By.ID, 'sign_in_v2_href').click()
time.sleep(2)

driver.find_element(By.ID, 'userName').send_keys(username)
time.sleep(1)
driver.find_element(By.ID, 'verify_user_btn').click()

time.sleep(5)
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(2)
driver.find_element(By.ID, 'btnSubmit').click()

driver.get('Past the link to the folder to where the files to be downlaoded')
time.sleep(10)

# Select all files in the diroctory 
select = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[1]/label')
select.click()

# Click to bring up the list of actions (Download, etc...)
list = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]')
list.click()

# Download selected files
download = driver.find_element(By.XPATH, "/html/body/div[@class='sc-fPXMVe hIKjlT']/ul[@class='sc-fHjqPf kywtBP']/li[@class='sc-feUZmu izpaYe'][7]/div[@class='sc-ikkxIA fOReae sc-fUnMCh irDTXf']")
download.click()

# Confirm the downlaod action
confirm = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div/footer/div/div/button")
confirm.click()

time.sleep(25)





