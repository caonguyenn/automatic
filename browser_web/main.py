import sys;sys.path.append("/home/caonguyen/automatic/browser_web")
from lib.base_selenium import BaseSelenium
import unittest

web_link = "http://automated.pythonanywhere.com/"


class SelenuimTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        open("element.txt", "w").close()
        cls.element = BaseSelenium(web_link)


    def tets_a_login_and_back_home(self):
        rc = self.element.click_element("xpath", "/html/body/nav/div/div/div/a")
        self.assertEqual(rc, 0, "Error to click element login.")

        rc = self.element.login("id", "automated", "automatedautomated", "id_username", "id_password")
        self.assertEqual(rc, 0, "Error to login.")

        rc = self.element.click_element("xpath", "/html/body/nav/div/a")
        self.assertEqual(rc, 0, "Error to click element home.")

    def test_get_element(self):
        self.get_text("xpath", "/html/body/div[1]/div/h1[1]")
        self.get_text("xpath", "/html/body/div[1]/div/h1[2]")

    def get_text(self, method, element):
        text = self.element.get_element(method, element)
        #TODO: self.assertEqual(text, str, "Error to get element")
        self.write_file(text)

    @staticmethod
    def write_file(text):
        """Write text into the .txt file"""
        file_name = f"element.txt"
        with open(file_name, "a") as file:
            file.write(text + "\n")
    
if __name__ == "__main__":
    unittest.main()



