from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# driver_path = "/home/caonguyen/driver/chromedriver"
service = Service("/home/caonguyen/driver/chromedriver")


class BaseSelenium():
    def __init__(self, web_link):
        self.web_link = web_link
        self.driver = self.get_driver()

    def get_driver(self):
        """
            Get driver from a website

            parameter:
                weblink(str): link of one website (ex:http://automated.pythonanywhere.com/)
        """
        # set option to make browsing easier
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars") # to disable infobars
        options.add_argument("start-maximized") # will start the browser as maximized
        options.add_argument("disable-dev-shm-usage") #This particular option is to avoid some issues that occur when you interact with a browser on a Linux computer
        options.add_argument("no-sanbox") # security the browser
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_argument("disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.web_link)

        return driver
    
    def get_element(self, element_type, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((element_type, element)))
        element = self.driver.find_element(element_type, element)
        return element.text
    
    def login(self, element_type, uname, pwd, idn, idp):
        self.driver.find_element(element_type, idn).send_keys(uname)
        self.driver.find_element(element_type, idp).send_keys(pwd + Keys.ENTER)
        return 0

    def click_element(self, element_type, element):
         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((element_type, element)))
         self.driver.find_element(element_type, element).click()
         return 0
