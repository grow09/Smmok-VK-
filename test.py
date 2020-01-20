import time
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions() 
prefs = {"profile.managed_default_content_settings.images":2} 
chromeOptions.add_experimental_option("prefs",prefs) 
driver = webdriver.Chrome(chrome_options=chromeOptions) 


# base https://docs.google.com/spreadsheets/d/1a6h0-yYMyq11njW-xIh1Q0B5OAYZbZ5rVHYq-L5CGLI/edit?usp=sharing

def logining():
    driver.get("https://smmok14.ru/")
    driver.find_element_by_xpath("//a[@x-ulogin-button='vkontakte']").click()
    driver.switch_to_window(driver.window_handles[1])
    # driver.find_element_by_xpath("//input[@type='text']").send_keys("380634754224")
    # driver.find_element_by_xpath("//input[@type='password']").send_keys("ghkfhk3347568")
    driver.find_element_by_xpath("//input[@type='text']").send_keys("380916166800")
    driver.find_element_by_xpath("//input[@type='password']").send_keys("sfghsgh46346")
    driver.find_element_by_class_name("oauth_button").click()
    driver.switch_to_window(driver.window_handles[0])
    driver.get("https://smmok14.ru/offer/index")
    driver.find_element_by_class_name("ui-dialog-buttonset").click() 

def working():
    project_name = driver.find_element_by_xpath("//span[@class='project_name']").text
    print(project_name)
    if project_name == "Добавить в друзья":
        add_friend()
    elif project_name == "Подписка":
        subscribe()
    elif project_name == "Просмотр страницы":
        look()
    elif project_name == "Мне нравится":
        like()
    elif project_name == "Лайк + рассказать друзьям":
        like_repost()
    else:
        time.sleep(13)
        working()

def add_friend():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//button[@class='flat_button button_wide']").click()
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()

def subscribe():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//button[@id='join_button']").click()
    except:
        second_chance()
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        # driver.find_element_by_xpath("//a[@class='ui-icon ui-icon-closethick']").click()
        # time.sleep(5)
        # working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()

def second_chance():
    try:
            driver.find_element_by_xpath("//button[@id='public_subscribe']").click()
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()

def look():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(5)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    try:
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(10)
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//a[@class='ui-dialog-titlebar-close ui-corner-all']").click()
        time.sleep(5)
        working()
    print("wohoo")
    working()

def like():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//a[@class='like_btn like _like']").click()
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//a[@class='ui-dialog-titlebar-close ui-corner-all']").click()
        time.sleep(5)
        working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()
    
def like_repost():  
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//a[@class='like_btn share _share']").click()
        time.sleep(3)
        driver.find_element_by_class_name("radiobtn").click()
        driver.find_element_by_xpath("//button[@class='like_share_btn flat_button']").click()
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//a[@class='ui-dialog-titlebar-close ui-corner-all']").click()
        time.sleep(5)
        working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()
  
if __name__ == '__main__':
    try:
        logining()
        working()
        add_friend()
        second_chance()
        subscribe()
        look()
        like()
        like_repost() 
    except:
        pass