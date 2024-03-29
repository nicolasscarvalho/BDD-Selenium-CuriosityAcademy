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

        #self.driver.fullscreen_window()

        #self.driver.execute_script("document.body.style.zoom='50%'")

        """
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for i in range(0,5):
            body.send_keys(Keys.CONTROL + '-')
        """

    def first_name(self, name: str): # REQUIRED FIELD
        if name == '':
            print('Campo "first name" inválido')
            return False #return False #raise ValueError('Campo "first name" inválido')
        
        element = self.driver.find_element(By.ID, 'firstName')
        element.send_keys(name)
        return True

    def last_name(self, last_name: str): # REQUIRED FIELD
        if last_name == '':
            print('Campo "last name" inválido')
            return False #raise ValueError('Campo "last name" inválido')
        
        element = self.driver.find_element(By.ID, 'lastName')
        element.send_keys(last_name)
        return True

    def email(self, email: str): # REQUIRED FIELD
        if email == '' or not(email.endswith('@gmail.com')):
            print('Campo "email" inválido')
            return False #raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.ID, 'userEmail')
        element.send_keys(email)
        return True

    def gender(self, gender: int): # REQUIRED FIELD
        if gender < 1 or gender > 3:
            print('Campo "gender" inválido')
            return False #raise ValueError('Campo "gender" inválido')
        
        element = self.driver.find_element(By.CSS_SELECTOR, f'label[for="gender-radio-{gender}"]')
        element.click()
        return True

    def mobile(self, mobile: str): # REQUIRED FIELD
        if mobile == '' or len(mobile) > 10:
            print('Campo "mobile" inválido')
            return False #raise ValueError('Campo "mobile" inválido')
        
        element = self.driver.find_element(By.ID, 'userNumber')
        element.send_keys(mobile)
        return True

    def date_of_birth(self, day: int, month: int, year: int): # REQUIRED FIELD
        if day < 1 or month < 1 or year < 0 or day > 31 or month > 12:
            print('Campo "date of birth" inválido')
            return False #raise ValueError('Campo "date of birth" inválido')

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        element = self.driver.find_element(By.ID, 'dateOfBirthInput')
        element.send_keys(f'{day} {month_list[month-1]} {year}', Keys.ENTER)

        return True
 
    def subjects(self, subjects):
        if subjects == '':
            print('Campo "subjects" inválido')
            return False #raise ValueError('Campo "subjects" inválido')
         
        element = self.driver.find_element(By.ID, 'subjectsInput')
        element.send_keys(subjects)
        return True

    def hobbies(self, hobbies: int): # REQUIRED FIELD
        if hobbies not in [1,2,3]:
            print('Campo "hobbies" inválido')
            return False #raise ValueError('Campo "hobbies" inválido')
        
        element = self.driver.find_element(By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{hobbies}"]')
        element.click()
        return True

    def picture(self, picture_path: str):
        if picture_path == '':
            print('Campo "picture" inválido') 
            return False #raise ValueError('Campo "picture" inválido')

        element = self.driver.find_element(By.ID, 'uploadPicture')
        element.send_keys(picture_path)
        return True

    def current_address(self, current_address: str): # REQUIRED FIELD
        if current_address == '':
            print('Campo "email" inválido')
            return False #raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.ID, 'currentAddress')
        element.send_keys(current_address)
        return True

    def state_and_city(self):
        pass

    def submit_and_close_website(self):
        self.driver.find_element(By.ID, 'userForm').submit()

        try:
            confirmation = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div').is_displayed()
            self.driver.close()
            return True
        except:
            self.driver.close()
            print('Elemento não encontrado')
            return False #raise NoSuchElementException