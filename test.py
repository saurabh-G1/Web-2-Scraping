from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Method 1: Using a raw string
path = r"C:\Users\saurabh.gaud\Downloads\chromedriver"

# Create the Service object
service = Service(executable_path=path)

# Proceed with further Selenium WebDriver setup as needed
driver = webdriver.Chrome(service=service)
