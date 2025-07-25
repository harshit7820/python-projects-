from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

# Install and start the ChromeDriver
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://www.instagram.com")
time.sleep(10)

# Locate and interact with login elements
username = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(input("Enter your username: "))
print("Enter your Password: ")
password = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
pswd = getpass()
password.send_keys(pswd)
login_button = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[3]')
login_button.click()
time.sleep(10)

# Search for a user
search_bar = chrome.find_element("xpath", '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys(input("Enter the username of the other person: "))
time.sleep(7)
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# Interact with posts
post = chrome.find_element("xpath", '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
post.click()
time.sleep(2)
like_button = chrome.find_element("xpath", '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like_button.click()
next_button = chrome.find_element("xpath", '/html/body/div[5]/div[1]/div/div/a')
next_button.click()
time.sleep(2)

# Loop to like posts
while True:
    try:
        like_button = chrome.find_element("xpath", '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like_button.click()
        next_button = chrome.find_element("xpath", '/html/body/div[5]/div[1]/div/div/a[2]')
        next_button.click()
        time.sleep(5)
    except:
        close_button = chrome.find_element("xpath", '/html/body/div[5]/div[3]/button')
        close_button.click()
        break
