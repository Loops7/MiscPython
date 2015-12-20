from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import time
import os


#url = input("Enter URL of 1st Video in Playlist:\n")
#profile = FirefoxProfile('C:/Users/Joey/AppData/Local/Mozilla/Firefox/Profiles/')
driver = webdriver.Firefox()

#browser = webdriver.Firefox() sjtdhbgr.Selenium C:/Users/Joey/AppData/Local/Mozilla/Firefox/Profiles/eamh4i2c.default'
#url = "https://www.youtube.com/watch?v=qyI7QAnaVQQ&list=PLQ5ViwnWZ_8rM1YCg9b0RifwAslxdlzeh"
#url = "https://www.youtube.com/watch?v=uI5fks_or6Q&list=PL0O9yK6vMB1P_tzc_jfXn6Cw6Qr6KaEas"

driver.get('https://www.youtube.com/watch?v=l1lJBLNQXkQ&list=PLTS-digh3UNjN1KHqS62grVMfluVT-0Mt')

youtube_prefix = "https://www.youtube.com/watch?v="
urls, titles = [],[]
play_list = driver.find_elements(By.CLASS_NAME,'yt-uix-scroller-scroll-unit')
for video in play_list:
    titles.append(video.get_attribute('data-video-title'))
    urls.append(youtube_prefix + video.get_attribute('data-video-id')) 
  
titles = [title.replace('/',' ') for title in titles]   

SONGS_DIR = os.path.join('C:/Users/Joey/Music/', 'songs/')
if not os.path.exists(SONGS_DIR):
    os.makedirs(SONGS_DIR)
     
num = 0
for url in urls:
    yt_mp3 = "http://www.youtube-mp3.org/"   
    driver.get(yt_mp3)    
    

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,'submit')) and EC.element_to_be_clickable((By.ID,'youtube-url')))
    form = driver.find_element(By.ID, 'youtube-url')
    form.clear()
    form.send_keys(url)
    form.submit()

    dl_link = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#dl_link a[href*="create"')))
    #driver.get(dl_link.get_attribute('href'))
    
    print(num+1
          )
    with open(SONGS_DIR + str(num + 1) + " " + titles[num] + ".mp3" , "wb") as out:
        song = requests.get(dl_link.get_attribute('href'))
        for block in song.iter_content(1024):
            out.write(block)
            
        print(song.url)
    
    num += 1 
    time.sleep(10)
    
    