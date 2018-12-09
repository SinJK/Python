from selenium import webdriver 
from time import sleep 

usr = "sfrsux"
pwd = "****"
tweet = """

Content of tweet

"""
driver = webdriver.Firefox()
driver.get('https://twitter.com/login')
print ("Opened twitter...")
sleep(1) 
  
username_box = driver.find_element_by_class_name("js-username-field")
username_box.send_keys(usr) 

print ("Username entered") 
sleep(1) 
  
password_box = driver.find_element_by_class_name('js-password-field') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_class_name("EdgeButtom--medium") 
login_box.click() 
  
print ("Done") 

tweet_box = driver.find_element_by_id("global-new-tweet-button") 
tweet_box.click() 
print ("click pour tweet") 
sleep(1) 
tw2=driver.find_element_by_class_name("tweet-box-content")
tweet_input = tw2.find_element_by_class_name("rich-editor")
tweet_input.send_keys(tweet)

print ("tweet content added") 

tweet_btn = tw2.find_element_by_class_name("SendTweetsButton")
sleep(2)
tweet_btn.click()


input('Press anything to quit') 
driver.quit() 
print("Finished") 

