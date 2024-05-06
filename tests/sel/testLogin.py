from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class testLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        self.driver.quit()
        
    def testLoginCorrect(self):
        self.driver.get("https://ccsa-grupo-5.onrender.com")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"/html/body/main/div/h1").text,"Bienvenido a tu Aplicación")
        
    def testLoginWrong(self):
        self.driver.get("https://ccsa-grupo-5.onrender.com")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("10101010")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("9")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"/html/body/div[2]/form/div[3]").text,"Acceso inválido. Por favor, inténtelo otra vez.")
        
        

if __name__ == "__main__":
    unittest.main()
    
    
        
        
            