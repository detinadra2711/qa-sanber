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
    
    def test_g_Vacancies(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)

        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
        browser.find_element(By.ID, "menu_recruitment_viewJobVacancy").click()
        time.sleep(1)
        
        select = Select(browser.find_element(By.ID, 'vacancySearch_jobTitle'))
        select.select_by_value('26')
        time.sleep(1)
            
   
    def tearDown(self):
        self.browser.close()



if __name__ == "__main__":
    unittest.main()
