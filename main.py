import names
from selenium import webdriver
import tempMail2
import clipboard
import  time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"



for i in range(0,50):
    browser = webdriver.Chrome(desired_capabilities=capa)
    wait = WebDriverWait(browser, 20)
    browser.get('https://temp-mail.org/')
    time.sleep(5)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input')))
    time.sleep(5)
    browser.execute_script("window.stop();")
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button').click()
    time.sleep(1)
    email=clipboard.paste()
    print(email)

    browser.get('https://internshala.com/biggest-recruitment-fair?utm_source=eap_copylink&utm_medium=lrf1893164')
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[22]/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/input')))
    time.sleep(2)
    browser.find_element_by_id('email').send_keys(email)
    browser.find_element_by_id('password').send_keys('INTERNSHALA123')
    browser.find_element_by_id('first_name').send_keys(names.get_first_name())
    browser.find_element_by_id('last_name').send_keys(names.get_last_name())
    #browser.find_element_by_name('degree_type').click()
    #browser.find_element_by_xpath('//*[@id="degree_study"]/option[2]').click()
    browser.find_element_by_xpath('/html/body/div[1]/div[22]/div[1]/div[2]/div[2]/div[2]/div/form/button').click()
    time.sleep(10)
    browser.get('https://temp-mail.org/')
    time.sleep(15)
    browser.execute_script("window.scrollTo(0, 700)")
    browser.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[4]/ul/li[2]/div[3]/div[2]/a').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/a').click()
    time.sleep(4)
    browser.close()
    time.sleep(3)
