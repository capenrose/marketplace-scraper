import csv, time
from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver =  webdriver.Chrome()
web_driver.get("https://www.facebook.com/marketplace/category/computers?deliveryMethod=local_pick_up&exact=false")

#Code for automatically logging in
#-------------------------------------------------------#
#time.sleep(5)
#username_field = web_driver.find_element(By.ID,'_r_11_')
#password_field = web_driver.find_element(By.ID,'_r_15_')

#username_field.send_keys("Username Goes Here")
#password_field.send_keys("Password Goes Here")

#web_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div/div/div[5]/div').click()
#-------------------------------------------------------#

#Do Captcha
input("Press Enter after completing ReCaptcha/Logging in")

#Create File
file = open("marketplace.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(["PRICE", "TITLE","DESCRIPTION","LOCATION","TIME","LINK","SELLER"])
file.close()

def WriteToSheet(title,price,location,description,time,seller,link):
    file = open("marketplace.csv", "a", newline='')
    writer = csv.writer(file)
    writer.writerow([price, title, description, location, time, link, seller])
    file.close()

#Main Loop
current_listing_num = 0

for x in range(0,20):
    web_driver.execute_script("window.scrollBy(0, 250);")
    current_listing_num += 1
    time.sleep(2)
    print(current_listing_num)
    
    listing_time = "None"
    listing_location = "Shipping"

    #Visit Listing Page
    try:
        listing_link = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[{current_listing_num}]/div/div/span/div/div/div/div/a').get_attribute('href')
        web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[{current_listing_num}]/div/div/span/div/div/div/div/a').click()

        time.sleep(2)
        listing_price = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/span').text
        listing_title = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/h1/span').text
        try:
            listing_location = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/div[2]/div[4]/div/div/div[1]/span/span').text
        except:
            print("No listing locatin provided")
        listing_description = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/div[2]/div[1]/div/span').text
        try:
            listing_time = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/span/span/span/abbr/span').text
        except:
            print("No listing time provided")
        #Get Seller page link
        web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/span/span/div/span/div/a').click()
        time.sleep(2)
        listing_seller = web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/a').get_attribute('href')

        #Show Data
        print(listing_price)
        print(listing_title)
        print(listing_location)
        print(listing_description)
        print(listing_time)
        print(listing_seller)
        
        for index, c in enumerate(listing_title):
            if c == '"':
                listing_title = f'{listing_title[:index]}"{listing_title[index:]}'

        WriteToSheet(listing_title,listing_price,listing_location,listing_description,listing_time,listing_seller,listing_link)

        #Exit Listing Page
        web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div').click()
        web_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div').click()
    
    #Try failed, so the "listing" was a sponsorship.
    except Exception as e:
        print("Sponsorship")
        #Close profile window if it is open
        try:
            web_driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div').click()
        except:
            continue
        #Close listing window if it is open
        try:
            web_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div').click()
        except:
            continue
        
input("Press 'Enter' to close the script.")