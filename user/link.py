from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

# f : Cab or Bus (1= Cab, 2=Bus)
def get_link(source,destination,date_tr,time_tr,f):

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

    browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/span/div/div/div/div[2]').click()
    browser.find_element("xpath",'//*[@id=":9"]/div').click()
    date=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span[1]').text
    if(int(date[-1])!=int(date_tr)):
        diff=int(date_tr)-int(date[-1])
        for i in range(diff):
            browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span[2]/button[2]').click()
    
    time_n=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[1]/input')
    time_n.send_keys(Keys.CONTROL + "a")
    time_n.send_keys(Keys.DELETE)
    time_n.send_keys(time_tr)
    time.sleep(2)

    if(f==2):
	    browser.find_element("xpath",'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[3]/button').click()
            time.sleep(2)

    browser.find_element("xpath",'//*[@id="section-directions-trip-title-0"]').click()
    time.sleep(2)

    if(f==2):
	    route=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]').text
        info=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div').text
	    route=route+" , "+info
    else:
	    route="Cab"

    share=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/button')
    share.click()
    time.sleep(2)
    emb=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]')
    emb.click()
    time.sleep(4)
    link=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/input').get_attribute("value")
    return(route,link)
