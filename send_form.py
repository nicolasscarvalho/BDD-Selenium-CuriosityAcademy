from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class SendForm:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.options)
        self.driver.get("https://demoqa.com/automation-practice-form")

    def first_name(self, name: str): # REQUIRED FIELD
        if name == '':
            raise ValueError('Campo "first name" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        element.send_keys(name)
        return True

    def last_name(self, last_name: str): # REQUIRED FIELD
        if last_name == '':
            raise ValueError('Campo "last name" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="lastName"]')
        element.send_keys(last_name)
        return True

    def email(self, email: str): # REQUIRED FIELD
        if email == '' or not(email.endswith('@gmail.com')):
            raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')
        element.send_keys(email)
        return True

    def gender(self, gender: int): # REQUIRED FIELD
        if gender < 1 or gender > 3:
            raise ValueError('Campo "gender" inválido')
        
        element = self.driver.find_element(By.XPATH, f'//*[@id="genterWrapper"]/div[2]/div[{gender}]')
        element.click()
        return True

    def mobile(self, mobile: str): # REQUIRED FIELD
        if mobile == '' or len(mobile) > 10:
            raise ValueError('Campo "mobile" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="userNumber"]')
        element.send_keys(mobile)
        return True

    def date_of_birth(self, day: int, month: int, year: int): # REQUIRED FIELD
        if day < 1 or month < 1 or year < 0 or day > 31 or month > 12:
            raise ValueError('Campo "date of birth" inválido')

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        element = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        element.send_keys(f'{day} {month_list[month-1]} {year}')
        return True
 
    def subjects(self, subjects):
        if subjects == '':
            raise ValueError('Campo "subjects" inválido')
         
        element = self.driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
        element.send_keys(subjects)
        return True

    def hobbies(self, hobbies: int): # REQUIRED FIELD
        if hobbies not in [1,2,3]:
            raise ValueError('Campo "hobbies" inválido')
        
        element = self.driver.find_element(By.XPATH, f'//*[@id="hobbiesWrapper"]/div[2]/div[{hobbies}]')
        element.click()
        return True

    def picture(self, picture_path: str):
        if picture_path == '':
            raise ValueError('Campo "picture" inválido')

        element = self.driver.find_element(By.XPATH, '//*[@id="uploadPicture"]')
        element.send_keys(picture_path)
        return True

    def current_address(self, current_address: str): # REQUIRED FIELD
        if current_address == '':
            raise ValueError('Campo "email" inválido')
        
        element = self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
        element.send_keys(current_address)
        return True

    def state_and_city(self):
        pass

    def submit_and_close_website(self):
        send_btn = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        send_btn.click()

        confirmation = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div')
        
        if not confirmation.is_displayed():
            raise NoSuchElementException
        
        self.driver.close()
        return True