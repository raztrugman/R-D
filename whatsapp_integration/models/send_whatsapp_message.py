from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from odoo import api, fields, models
from selenium import webdriver
import time


class SendWhatsappMessage(models.TransientModel):
    _name = "send.whatsapp.message"
    _description = "Integration to whatsapp"

    contacts_numbers = fields.One2many('res.partner', 'name', string="WhatsApp Message Contacts Phone Numbers")

    def send_whatsapp_message(self):
        contact = "John"
        text = "Hey, this message was sent using Selenium"
        driver = webdriver.Chrome('whatsapp_integration,static/chromedriver/linux64bit/chromedriver')
        driver.get("https://web.whatsapp.com")
        print("Scan QR Code, And then Enter")
        input()
        print("Logged In")
        inp_xpath_search = "//input[@title='Search or start new chat']"
        input_box_search = WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element_by_xpath(inp_xpath_search))
        input_box_search.click()
        time.sleep(2)
        input_box_search.send_keys(contact)
        time.sleep(2)
        selected_contact = driver.find_element_by_xpath("//span[@title='" + contact + "']")
        selected_contact.click()
        inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)
        input_box.send_keys(text + Keys.ENTER)
        time.sleep(2)
        driver.quit()




"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options


WAITTIMEOUT=600
URL="https://web.whatsapp.com/"


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument('--disable-gpu') 
chrome_options.add_argument('"user-agent=Chrome/71.0.3578.98"')
chrome_driver = "/home/raz/Desktop/פיתוחים/R&D/WhatsApp Integration/chromedriver/linux64bit/chromedriver"

contacts = ["972546519123", "972546519123", "972546519123"]
for contact in contacts:
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    contact = "972546519123"
    phone_url = 'https://web.whatsapp.com/send?phone='+contact
    driver.get(phone_url)

    print("\n\n****\n\n    ")
    print(driver.capabilities)
    print("\n\n\n")

    print("browserVersion:    "+driver.capabilities.get('browserVersion'))
    print("chromedriverVersion:    "+driver.capabilities.get('chrome').get('chromedriverVersion'))



    text = str(datetime.now())

    print("****   ",driver.title)
    time.sleep(7)
    driver.get_screenshot_as_file('pic.png')

    wait = WebDriverWait(driver, WAITTIMEOUT)
    inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

    print(input_box, "          ****")
    input_box.click()
    input_box.send_keys(text + Keys.ENTER)
    print("****")

    time.sleep(2)
    driver.close()




"""




