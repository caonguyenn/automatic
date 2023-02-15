import sys;sys.path.append("/home/caonguyen/automatic/browser_web")
from lib.base_selenium import BaseSelenium

web_link = "http://automated.pythonanywhere.com/"
    
    
if __name__ == "__main__":
    robot = BaseSelenium(web_link)
    robot.click_element("xpath", "/html/body/nav/div/div/div/a")
    robot.login("id", "automated", "automatedautomated", "id_username", "id_password")
    robot.click_element("xpath", "/html/body/nav/div/a")
    print(robot.get_element("xpath", "/html/body/div[1]/div/h1[1]"))
    print(robot.get_element("xpath", "/html/body/div[1]/div/h1[2]"))


