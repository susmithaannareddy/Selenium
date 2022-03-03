from _ast import Assert
from datetime import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#Login to Flipkart Application and maximize the window
driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.flipkart.com/")
driver.maximize_window()


#Enter the User name and Password and goes to the Grocery section
text = driver.find_element(by=By.XPATH, value="//div[@class='IiD88i _351hSN']//input[@type='text']");
text.send_keys("8919818041")
password = driver.find_element(by=By.XPATH, value="//input[@type='password']");
password.send_keys("Lokesh@1")
submitbutton=driver.find_element(by=By.XPATH, value="//div[@class='_1D1L_j']//button[@type='submit']");
submitbutton.click()
time.sleep(60)
grocerybutton = driver.find_element(by=By.XPATH, value="//div[text()='Grocery']");
grocerybutton.click()
time.sleep(60)
currentlocation=driver.find_element(by=By.XPATH, value="//button[text()='Current Location']");
currentlocation.click();

#Select the 3 items form the grocery section
driver.find_element(by=By.XPATH, value="(//button[@class='_2KpZ6l GX4Kov']//span[text()='Add Item'])[1]").click()
driver.find_element(by=By.XPATH, value="(//button[@class='_2KpZ6l GX4Kov']//span[text()='Add Item'])[2]").click()
driver.find_element(by=By.XPATH, value="(//button[@class='_2KpZ6l GX4Kov']//span[text()='Add Item'])[3]").click()

a = ActionChains(driver)
m = driver.find_element(by=By.XPATH, value="//div[text()='My Account']")
a.move_to_element(m).click().perform()
# Getting current URL source code
loginPageTitle = driver.title
print(loginPageTitle)
searchtext = driver.find_element(by=By.XPATH, value="//input[@title='Search for products, brands and more']")

#filtering the items by using Besan Keyword
searchtext.send_keys("Besan")
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

FashionKeyword=driver.find_element(by=By.XPATH, value="//div[text()='Fashion']")
FashionKeyword.click();

ManageAdresses=driver.find_element(by=By.XPATH, value="//div[text()='Manage Addresses']")
ManageAdresses.click();

AddAdresses=driver.find_element(by=By.XPATH, value="//button[text()='ADD ADDRESSES']")
AddAdresses.click();

#Add the new Adresses
name=driver.find_element(by=By.XPATH, value="//input[@name='name']")
name.send_keys("Sushmitha")
Phone=driver.find_element(by=By.XPATH, value="//input[@name='phone']")
Phone.send_keys("8919818041")
Pincode=driver.find_element(by=By.XPATH, value="//input[@name='pincode']")
Pincode.send_keys("560076")
Locality=driver.find_element(by=By.XPATH, value="//label[text()='Locality']")
Locality.send_keys("Bangalore")
AreaandStreet=driver.find_element(by=By.XPATH, value="//label[text()='Address (Area and Street)']")
AreaandStreet.send_keys("BTM2ndstage")
Town=driver.find_element(by=By.XPATH, value="//label[text()='City/District/Town']")
Town.send_keys("Bangalore")
SaveButton=driver.find_element(by=By.XPATH, value="//button[text()='Save']")
SaveButton.click()

# Test logout functionality
LogoutButton=driver.find_element(by=By.XPATH, value="//span[text()='Logout']")

# Quitting the driver
driver.quit();
