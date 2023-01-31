from selenium import webdriver
import csv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()

username=' ' 
password=' '

usernames = ['kahlan_al_kharosi','kahlan_al_kharosi']

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(5)

browser.find_element("name","username").send_keys(username)
browser.find_element("name","password").send_keys(password)
browser.find_element("name","password").send_keys(Keys.RETURN)
print('done')
time.sleep(5)

with open('Accounts_Info.csv','a',newline='') as file:

    writer = csv.writer(file)

    writer.writerow(['username','followers','following','posts'])

    for username in usernames: 
        print(f'open {username} page')

        browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(10)
        
        followers = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span").text
        following = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/div/span/span").text
        posts = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span").text
        print(f"followers: {followers}")
        print(f"following: {following}")
        print(f"posts: { posts}")
        print("----------------------------")

        #follow
        follow_btn = browser.find_element_by_css_selector("button._acan._acap._acas._aj1-")
        follow_btn.click()
        print(f"following {username}")

        
        # finds the first picture
        post = browser.find_element_by_css_selector("div._ac7v._aang")
       
        num_post = 1 
       
    
        time.sleep(4)
        post.click()   # clicks on the first picture

        time.sleep(4)
        while (num_post < int(posts)):
            
            #Like
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
            
            #next post
            browser.find_element_by_css_selector(" div._aaqg._aaqh").click() 
            
            time.sleep(4)

            num_post= num_post+1

        writer.writerow([username,followers , following, posts])
   

  


