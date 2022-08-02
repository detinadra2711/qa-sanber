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
                
    def test_i_Maintenance(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)

        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_maintenance_purgeEmployee").click()
        browser.find_element(By.ID, "menu_maintenance_PurgeRecords").click()
        browser.find_element(By.ID, "menu_maintenance_purgeEmployee").click()
        time.sleep(1)
        browser.find_element(By.ID, "confirm_password").send_keys("qwerty")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "#frmPurgeEmployeeAuthenticate > div > div > input[type=submit]")
        time.sleep(2)
        
   
    def tearDown(self):
        self.browser.close()



if __name__ == "__main__":
    unittest.main()
