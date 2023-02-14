from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# driver_path = "/home/caonguyen/driver/chromedriver"
service = Service("/home/caonguyen/driver/chromedriver")
def get_driver(weblink):
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
    driver.get(weblink)

    return driver

def print_element(weblink, xpath):
    driver = get_driver(weblink)
    for xpath in xpath:
        time.sleep(1)
        element = driver.find_element("xpath", xpath)
        print(element.text)

if __name__ == "__main__":
    weblink = "http://automated.pythonanywhere.com/"
    xpath_main_element = "/html/body/div[1]/div/h1[1]"
    xpath_temperature_element = "/html/body/div[1]/div/h1[2]"
    print_element(weblink, [xpath_main_element, xpath_temperature_element])