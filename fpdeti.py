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
        
    def test_a_login(self):
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(3)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        
        response_message = browser.find_element(By.ID, "menu_admin_viewAdminModule").text
        self.assertEqual(response_message, 'Admin')
        
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
        
    def test_b_JobStatus(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
    
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_admin_viewAdminModule").click()
        browser.find_element(By.ID, "menu_admin_Job").click()
        browser.find_element(By.ID, "menu_admin_employmentStatus").click()
        browser.find_element(By.ID, "btnAdd").click()
        browser.find_element(By.ID, "empStatus_name").send_keys("tes")
        time.sleep(1)
        browser.find_element(By.ID, "btnSave").click()
        time.sleep(1)
        
    def test_c_AddEmployee(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
    
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_pim_viewPimModule").click()
        browser.find_element(By.ID, "menu_pim_addEmployee").click()
        time.sleep(1)

    def test_d_Skills(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
        
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_admin_viewAdminModule").click()
        browser.find_element(By.ID, "menu_admin_Qualifications").click()
        browser.find_element(By.ID, "menu_admin_viewSkills").click()
        browser.find_element(By.ID, "btnAdd").click()
        browser.find_element(By.ID, "skill_name").send_keys("Web Design")
        time.sleep(1)
        browser.find_element(By.ID, "skill_description").send_keys("Programming")
        time.sleep(1)
        browser.find_element(By.ID, "btnSave").click()
        time.sleep(1)
        
    def test_e_Leave(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
        
        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_leave_viewLeaveModule").click()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        browser.find_element(By.ID, "menu_leave_applyLeave")
        time.sleep(2)
        
    def test_f_Timesheet(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)

        browser.find_element(By.ID, "txtUsername").send_keys("Admin")
        browser.find_element(By.ID, "txtPassword").send_keys("admin123")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        browser.find_element(By.ID, "menu_time_viewTimeModule").click()
        browser.find_element(By.ID, "menu_time_Timesheets").click()
        browser.find_element(By.ID, "menu_time_viewMyTimesheet").click()
        browser.find_element(By.ID, "startDates").click()
        browser.find_element(By.ID, "btnAddTimesheet").click()
        browser.find_element(By.ID, "time_date").click()
        browser.find_element(By.ID, "addTimesheetBtn").click()
    
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
