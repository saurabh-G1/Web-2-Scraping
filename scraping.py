from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import openpyxl
# type: ignore
# this bellow line is additional step we have to do in selinium4 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
# web variable having the link of the website we want to scrap
web = 'https://www.audible.com/search'
#path ='C:\Users\saurabh.gaud\Downloads\chromedriver'
#path = r'C:\Users\saurabh.gaud\Downloads\chromedriver'
path = r'C:\Users\saurabh.gaud\Downloads\chromedriver\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
# driver is variable to interact with the website to extract the data
driver = webdriver.Chrome(service=service)
# that's prity much it (i.e. the above lines)when working with selenium

driver.get(web)
# To write the xpath we need 3 elements i.e. tag_name, attribute_name and attribute_value.
book_title = []
book_author = []
book_length = []
            
def extract_products():
            products_list = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
            # print(products_list)
            for product in products_list:
                book_title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
                book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
                book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
                
extract_products()      

while True:
    try:
        # Try to find the "Next" button/link and click it
        next_button = driver.find_element(By.XPATH, '//span[contains(@class, "bc-text bc-button-text-inner bc-size-action-small")]')
        next_button.click()

        # Wait for the page to load (optional: use WebDriverWait for more robust waiting)
        driver.implicitly_wait(5)

        # Extract products on the new page
        extract_products()
    except NoSuchElementException:
        # If no "Next" button/link is found, break the loop
        break          
                    
   
df=pd.DataFrame({"book_title":book_title,'book_author':book_author,"book_length":book_length})  
# print(df) 
# df.to_excel('booker.xlsx', index=False)
df.to_csv('bookerr.csv', index=False)

     
driver.quit()


# WebElement element = driver.findElement(By.XPath(“//div[@id='myid']”))
# //h3[contains(@class,"bc-heading")]

# //li[contains(@class,"authorLabel")]

# //li[contains(@class,"runtimeLabel")]






















