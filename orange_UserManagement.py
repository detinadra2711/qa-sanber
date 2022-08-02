import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class TestOrange(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_UserManagement(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_admin_viewAdminModule").click()
        browser.find_element(By.ID, "menu_admin_UserManagement").click()
        browser.find_element(By.ID, "menu_admin_viewSystemUsers").click()
        time.sleep(1)
        browser.find_element(By.ID, "searchSystemUser_userName").send_keys("admin")
        browser.find_element(By.CLASS_NAME, "searchbutton").click()
        time.sleep(3)
        

        
   
    def tearDown(self):
        self.browser.close()



if __name__ == "__main__":
    unittest.main()
