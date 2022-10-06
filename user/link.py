from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

def get_link(source,destination):

    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.google.com/maps')
    box=browser.find_element("xpath",'//*[@id="searchboxinput"]')
    box.click()

    box.send_keys(destination) 
    box.send_keys(Keys.ENTER)
    time.sleep(4)

    dir=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
    dir.click()
    time.sleep(4)
    box=browser.find_element("xpath",'//*[@id="sb_ifc51"]/input')
    box.click()
    box.send_keys(source) 
    box.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element("xpath",'//*[@id="section-directions-trip-title-0"]').click()
    time.sleep(2)
    share=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/button')
    share.click()
    time.sleep(2)
    emb=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]')
    emb.click()
    time.sleep(4)
    link=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/input').get_attribute("value")
    return link