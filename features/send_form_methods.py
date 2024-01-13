from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class SendFormMethods:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.options)

        self.driver.get("https://demoqa.com/automation-practice-form")

        self.driver.fullscreen_window()

        self.driver.execute_script("document.body.style.zoom='50%'")

        """
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for i in range(0,5):
            body.send_keys(Keys.CONTROL + '-')
        """

    def first_name(self, name: str): # REQUIRED FIELD
        if name == '':
            return False #return False #raise ValueError('Campo "first name" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        element.send_keys(name)
        return True

    def last_name(self, last_name: str): # REQUIRED FIELD
        if last_name == '':
            return False #raise ValueError('Campo "last name" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="lastName"]')
        element.send_keys(last_name)
        return True

    def email(self, email: str): # REQUIRED FIELD
        if email == '' or not(email.endswith('@gmail.com')):
            return False #raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')
        element.send_keys(email)
        return True

    def gender(self, gender: int): # REQUIRED FIELD
        if gender < 1 or gender > 3:
            return False #raise ValueError('Campo "gender" inválido')
        
        element = self.driver.find_element(By.XPATH, f'//*[@id="gender-radio-{gender}"]')
        element.click()
        return True

    def mobile(self, mobile: str): # REQUIRED FIELD
        if mobile == '' or len(mobile) > 10:
            return False #raise ValueError('Campo "mobile" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="userNumber"]')
        element.send_keys(mobile)
        return True

    def date_of_birth(self, day: int, month: int, year: int): # REQUIRED FIELD
        if day < 1 or month < 1 or year < 0 or day > 31 or month > 12:
            return False #raise ValueError('Campo "date of birth" inválido')

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        element = self.driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
        element.send_keys(f'{day} {month_list[month-1]} {year}', Keys.ENTER)

        return True
 
    def subjects(self, subjects):
        if subjects == '':
            return False #raise ValueError('Campo "subjects" inválido')
         
        element = self.driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
        element.send_keys(subjects)
        return True

    def hobbies(self, hobbies: int): # REQUIRED FIELD
        if hobbies not in [1,2,3]:
            return False #raise ValueError('Campo "hobbies" inválido')
        
        element = self.driver.find_element(By.XPATH, f'//*[@id="hobbies-checkbox-{hobbies}"]')
        element.click()
        return True

    def picture(self, picture_path: str):
        if picture_path == '':
            return False #raise ValueError('Campo "picture" inválido')

        element = self.driver.find_element(By.XPATH, '//*[@id="uploadPicture"]')
        element.send_keys(picture_path)
        return True

    def current_address(self, current_address: str): # REQUIRED FIELD
        if current_address == '':
            return False #raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
        element.send_keys(current_address)
        return True

    def state_and_city(self):
        pass

    def submit_and_close_website(self):
        send_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        send_btn.click()

        try:
            confirmation = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div').is_displayed()
            self.driver.close()
            return True
        except:
            self.driver.close()
            return False #raise NoSuchElementException