import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

#  
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
   
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')
        
        
    def test_b_signup(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser = self.browser  # buka web browser
        browser.find_element(By.ID, "signUp").click()
        time.sleep(2)
        browser.find_element(By.ID, "name_register").send_keys("tester")
        time.sleep(2)
        browser.find_element(By.ID, "email_register").send_keys("tester@jagoqa.com")
        time.sleep(2)
        browser.find_element(By.ID, "password_register").send_keys("testerjago")
        time.sleep(2)
        browser.find_element(By.ID, "signup_register").click() # klik tombol sign up
        time.sleep(1)
        
        # validasi textnya
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text
        
        self.assertIn('Email sudah terdaftar', response_data)
        self.assertEqual(response_message, 'gagal')
        

    def test_a_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        

    def test_a_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')
        
        
    def test_a_failed_login_with_random_email(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("123")  # isi email tanpa @
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password").send_keys("testerqa")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    # lib bawaan dari unittest
    def tearDown(self): 
        self.browser.close() 

# utk menjalankan class nya
if __name__ == "__main__": 
    unittest.main() 