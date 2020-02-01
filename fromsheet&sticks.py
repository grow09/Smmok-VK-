import time
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

PROXY = 'your_proxy'


chromeOptions = webdriver.ChromeOptions() 
prefs = {"profile.managed_default_content_settings.images":2} 
chromeOptions.add_experimental_option("prefs",prefs) 
chromeOptions.add_argument('--proxy-server=%s' % PROXY) 
driver = webdriver.Chrome(chrome_options=chromeOptions) 

accounts = ['can','use','multiply','accounts'] # ["number", "pass", "number", "pass"]
i = 0
j = 1



def logining():
    driver.get("https://whoer.net")
    time.sleep(10)
    driver.get("https://smmok14.ru/")
    driver.find_element_by_xpath("//a[@x-ulogin-button='vkontakte']").click()
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_xpath("//input[@type='text']").send_keys(accounts[i])
    driver.find_element_by_xpath("//input[@type='password']").send_keys(accounts[j])
    driver.find_element_by_class_name("oauth_button").click()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.get("https://smmok14.ru/offer/index")
    time.sleep(10)
    driver.find_element_by_class_name("ui-dialog-buttonset").click() 
    working()

def working():
    global i
    global j
    time.sleep(3)
    try:
        project_name = driver.find_element_by_xpath("//span[@class='project_name']").text
    except:
        i = i+2
        j = j+2
        print(accounts[i])
        print(accounts[j])
        out_()
    print(project_name)
    driver.get("https://smmok14.ru/offer/index")
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
        time.sleep(300)
        working()
        

def add_friend():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='flat_button button_wide']").click()
        time.sleep(2)
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(12)
    print("wohoo")
    working()

def subscribe():
    driver.find_element_by_xpath("//a[@class='button projectDetails']").click()
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//button[@id='join_button']").click()
        time.sleep(2)
    except:
        second_chance()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()

def second_chance():
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//button[@id='public_subscribe']").click()
        time.sleep(2)
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(3)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
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
        time.sleep(3)
        driver.find_element_by_xpath("//button[2]").click()
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
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='like_btn like _like']").click()
        time.sleep(2)
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(3)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
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
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='like_btn share _share']").click()
        time.sleep(3)
        driver.find_element_by_class_name("radiobtn").click()
        driver.find_element_by_xpath("//button[@class='like_share_btn flat_button']").click()
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(5)
        working()
    time.sleep(3)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(10)
    print("wohoo")
    working()

def out_():
    driver.get("https://smmok14.ru/welcome/logout")
    driver.get("https://vk.com/")
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='top_profile_link']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='top_logout_link']").click()
    logining()

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
        out_()
    except:
        pass
