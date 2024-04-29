from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
import string


def generate_id():
    return str(random.randint(10000000, 99999999))

idGenerated = generate_id()

class testCreateUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        self.driver.quit()
        
    def random_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    
    def random_email(self):
        letters = string.ascii_lowercase
        domain = "@gmail.com"
        random_string = ''.join(random.choice(letters) for _ in range(10))
        return random_string + domain
    
    def testCreateLeaderUserCorrect(self):
        self.driver.get("http://127.0.0.1:8000/")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        createButton = self.driver.find_element(By.XPATH,"/html/body/nav/ul/li[2]/a")
        createButton.click()
        userId = self.driver.find_element(By.ID,"id_username")
        userId.send_keys(idGenerated)
        userName = self.driver.find_element(By.ID,"id_first_name")
        userName.send_keys(self.random_string(random.randint(5, 10)))
        userLastName = self.driver.find_element(By.ID,"id_last_name")
        userLastName.send_keys(self.random_string(random.randint(5, 10)))
        userEmail = self.driver.find_element(By.ID,"id_email")
        userEmail.send_keys(self.random_email())
        rol = self.driver.find_element(By.CSS_SELECTOR, "#id_roles option:nth-child(1)")
        rol.click()
        password = self.driver.find_element(By.ID,"id_password1")
        password.send_keys("passTi148")
        password2 = self.driver.find_element(By.ID,"id_password2")
        password2.send_keys("passTi148")
        registerButton =self.driver.find_element(By.XPATH,"/html/body/main/div/form/div/button")
        registerButton.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"/html/body/main/div/form/div[2]").text,"Usuario creado satisfactoriamente")
        
    def testCreateManagerUserCorrect(self):
        self.driver.get("http://127.0.0.1:8000/")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        createButton = self.driver.find_element(By.XPATH,"/html/body/nav/ul/li[2]/a")
        createButton.click()
        userId = self.driver.find_element(By.ID,"id_username")
        idCreated = generate_id()
        userId.send_keys(idCreated)
        userName = self.driver.find_element(By.ID,"id_first_name")
        userName.send_keys(self.random_string(random.randint(5, 10)))
        userLastName = self.driver.find_element(By.ID,"id_last_name")
        userLastName.send_keys(self.random_string(random.randint(5, 10)))
        userEmail = self.driver.find_element(By.ID,"id_email")
        userEmail.send_keys(self.random_email())
        rol = self.driver.find_element(By.CSS_SELECTOR, "#id_roles option:nth-child(2)")
        rol.click()
        password = self.driver.find_element(By.ID,"id_password1")
        password.send_keys("passTi148")
        password2 = self.driver.find_element(By.ID,"id_password2")
        password2.send_keys("passTi148")
        registerButton =self.driver.find_element(By.XPATH,"/html/body/main/div/form/div/button")
        registerButton.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"/html/body/main/div/form/div[2]").text,"Usuario creado satisfactoriamente")



    def testDuplicateUser(self):
        self.driver.get("http://127.0.0.1:8000/")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        createButton = self.driver.find_element(By.XPATH,"/html/body/nav/ul/li[2]/a")
        createButton.click()
        userId = self.driver.find_element(By.ID,"id_username")
        userId.send_keys(idGenerated)
        userName = self.driver.find_element(By.ID,"id_first_name")
        userName.send_keys(self.random_string(random.randint(5, 10)))
        userLastName = self.driver.find_element(By.ID,"id_last_name")
        userLastName.send_keys(self.random_string(random.randint(5, 10)))
        userEmail = self.driver.find_element(By.ID,"id_email")
        userEmail.send_keys(self.random_email())
        rol = self.driver.find_element(By.CSS_SELECTOR, "#id_roles option:nth-child(2)")
        rol.click()
        password = self.driver.find_element(By.ID,"id_password1")
        password.send_keys("passTi148")
        password2 = self.driver.find_element(By.ID,"id_password2")
        password2.send_keys("passTi148")
        registerButton =self.driver.find_element(By.XPATH,"/html/body/main/div/form/div/button")
        registerButton.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"/html/body/main/div/form/div[2]").text,"Error en Cedula: Ya existe Usuario con este Identificador.")
        

if __name__ == "__main__":
    unittest.main()
    
    
        
        
            