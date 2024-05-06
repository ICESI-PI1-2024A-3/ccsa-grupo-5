from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class testCreateRequest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        self.driver.quit()
        
    
        #2lasts+
        
    def testCreateMonitoringRequestCorrect(self):
        self.driver.get("https://ccsa-grupo-5.onrender.com")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        hMenu = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/div')
        hMenu.click()
        requestButton = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/ul/li[3]/a')
        requestButton.click()
        monitoringRequestButton = self.driver.find_element(By.XPATH,"/html/body/main/div/div[2]/div[1]/a/button")
        monitoringRequestButton.click()
        requestDate = self.driver.find_element(By.ID,"id_petitionDate")
        requestDate.send_keys("29/04/2024")
        requestStartDate = self.driver.find_element(By.ID,"id_startDate")
        requestStartDate.send_keys("2/05/2024")
        requestFinalDate = self.driver.find_element(By.ID,"id_endDate")
        requestFinalDate.send_keys("21/11/2024")
        #state = self.driver.find_element(By.CSS_SELECTOR, "#id_state option:nth-child(2)")
        #state.click()
        costCenter = self.driver.find_element(By.ID,"id_cenco")
        costCenter.send_keys("Centro 1")
        fullName = self.driver.find_element(By.ID,"id_fullName")
        fullName.send_keys("Andres Mauricio Mesa")
        documentId = self.driver.find_element(By.ID,"id_identityDocument")
        documentId.send_keys("101010101")
        email = self.driver.find_element(By.ID,"id_email")
        email.send_keys("DweynJhonson@gmail.com")
        cell = self.driver.find_element(By.ID,"id_phoneNumber")
        cell.send_keys("3127327141")
        user = self.driver.find_element(By.CSS_SELECTOR, "#id_user option:nth-child(1)")
        user.click()
        haveMoneyCheck = self.driver.find_element(By.ID, "id_hasMoneyInCenco")
        haveMoneyCheck.click()
        responsible = self.driver.find_element(By.ID, "id_cencoResponsible")
        responsible.send_keys("Oscar Ice")
        monitoringType = self.driver.find_element(By.CSS_SELECTOR, "#id_monitoringType option:nth-child(2)")
        monitoringType.click()
        studentCode = self.driver.find_element(By.ID, "id_studentCode")
        studentCode.send_keys("A00386327")
        daviPlata = self.driver.find_element(By.ID, "id_daviPlata")
        daviPlata.send_keys("3127327141")
        project = self.driver.find_element(By.ID, "id_projectOrCourse")
        project.send_keys("Apo")
        description = self.driver.find_element(By.ID, "id_monitoringDescription")
        description.send_keys("...")
        weeklyHours = self.driver.find_element(By.ID, "id_hoursPerWeek")
        weeklyHours.send_keys("4")
        paymentAmount = self.driver.find_element(By.ID, "id_totalPaymentAmount")
        paymentAmount.send_keys("500000")
        oneTimePayment = self.driver.find_element(By.ID, "id_isOneTimePayment")
        oneTimePayment.click()
        saveButton = self.driver.find_element(By.XPATH,"/html/body/main/div/form/button")
        saveButton.click()
        self.driver.implicitly_wait(10)
        hMenu2 = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/div')
        hMenu2.click()
        self.driver.implicitly_wait(10)
        viewRequest = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/ul/li[5]/a')
        viewRequest.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        requestAmount = Select(self.driver.find_element(By.XPATH,'//*[@id="dataTablePetition_length"]/label/select'))
        requestAmount.select_by_index(3)
        self.assertEqual(self.driver.find_element(By.XPATH,'//*[@id="dataTablePetition"]/tbody/tr[last()]/td[9]').text,"101010101")
        
        
    def testCreateServicesProvisionRequestCorrect(self):
        self.driver.get("https://ccsa-grupo-5.onrender.com")
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("4")
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("4")
        loginButton = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/button")
        loginButton.click()
        hMenu = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/div')
        hMenu.click()
        requestButton = self.driver.find_element(By.XPATH,'//*[@id="navbarContainer"]/ul/li[3]/a')
        requestButton.click()
        provisionRequestButton = self.driver.find_element(By.XPATH,"/html/body/main/div/div[2]/div[2]/a/button")
        provisionRequestButton.click()
        requestDate = self.driver.find_element(By.ID,"id_petitionDate")
        requestDate.send_keys("06/05/2024")
        requestStartDate = self.driver.find_element(By.ID,"id_startDate")
        requestStartDate.send_keys("8/05/2024")
        requestFinalDate = self.driver.find_element(By.ID,"id_endDate")
        requestFinalDate.send_keys("15/10/2024")
        state = self.driver.find_element(By.CSS_SELECTOR, "#id_state option:nth-child(2)")
        state.click()
        costCenter = self.driver.find_element(By.ID,"id_cenco")
        costCenter.send_keys("Centro 1")
        fullName = self.driver.find_element(By.ID,"id_fullName")
        fullName.send_keys("Daniel Ortega")
        documentId = self.driver.find_element(By.ID,"id_identityDocument")
        documentId.send_keys("1111470231")
        email = self.driver.find_element(By.ID,"id_email")
        email.send_keys("rock@gmail.com")
        cell = self.driver.find_element(By.ID,"id_phoneNumber")
        cell.send_keys("3127327141")
        user = Select(self.driver.find_element(By.ID,"id_user"))
        user.select_by_index(1)
        petitionType = Select(self.driver.find_element(By.ID,"id_personType"))
        petitionType.select_by_index(1)
        applicantName = self.driver.find_element(By.ID,"id_requesterName")
        applicantName.send_keys("Jorge Vidal")
        facultyApplicant = self.driver.find_element(By.ID,"id_requesterFaculty")
        facultyApplicant.send_keys("Facultad de Ingenieria y Ciencias Aplicadas")
        reason = self.driver.find_element(By.ID,"id_motive")
        reason.send_keys("Prácticas")
        banketingEntity = self.driver.find_element(By.ID,"id_bankEntity")
        banketingEntity.send_keys("DaviPlata")
        bankType = Select(self.driver.find_element(By.ID, "id_bankAccountType"))
        bankType.select_by_index(1)
        accountNumber = self.driver.find_element(By.ID,"id_bankAccountNumber")
        accountNumber.send_keys("3126238161")
        eps = self.driver.find_element(By.ID,"id_eps")
        eps.send_keys("Sura")
        pensionFound = self.driver.find_element(By.ID,"id_pensionFund")
        pensionFound.send_keys("No")
        arl = self.driver.find_element(By.ID,"id_arl")
        arl.send_keys("No")
        contractValue = self.driver.find_element(By.ID,"id_contractValue")
        contractValue.send_keys("1000000")
        infPay = self.driver.find_element(By.ID,"id_paymentInfo")
        infPay.send_keys("...")
        
        directory = os.path.dirname(os.path.abspath(__file__))
        imageRout = os.path.join(directory, "images", "rutSelenium.jpeg")
       
        rut = self.driver.find_element(By.ID,"id_rutAttachment")
        rut.send_keys(imageRout)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        self.driver.implicitly_wait(10)
        
        saveButton = self.driver.find_element(By.XPATH,"/html/body/main/div/form/button") 
        saveButton.click()
 
        self.driver.implicitly_wait(10)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        self.driver.implicitly_wait(10)
        requestAmount = Select(self.driver.find_element(By.NAME,"dataTablePetition_length"))
        requestAmount.select_by_index(3)
        self.assertEqual(self.driver.find_element(By.XPATH,'//*[@id="dataTablePetition"]/tbody/tr[last()]/td[9]').text,"1111470231")
        
        

if __name__ == "__main__":
    unittest.main()
    
    
        
        
            