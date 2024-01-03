from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SendForm:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.options)
        self.driver.get("https://demoqa.com/automation-practice-form")

    def first_name(self, name: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        element.send_keys(name)

    def last_name(self, last_name: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="lastName"]')
        element.send_keys(last_name)

    def email(self, email: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')
        element.send_keys(email)

    def gender(self, gender: int):
        gender_list = [
            self.driver.find_element(By.XPATH, '//*[@id="gender-radio-1"]'),
            self.driver.find_element(By.XPATH, '//*[@id="gender-radio-2"]'),
            self.driver.find_element(By.XPATH, '//*[@id="gender-radio-3"]')
        ]
        gender_list[gender].click()


    def mobile(self, mobile: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="userNumber"]')
        element.send_keys(mobile)

    def date_of_birth(self):
        pass

    def subjects(self, subjects):
        element = self.driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
        element.send_keys(subjects)

    def hobbies(self, hobbies: int):
        hobbies_list = [
            self.driver.find_element(By.XPATH, '//*[@id="hobbies-checkbox-1"]'),
            self.driver.find_element(By.XPATH, '//*[@id="hobbies-checkbox-2"]'),
            self.driver.find_element(By.XPATH, '//*[@id="hobbies-checkbox-3"]')
        ]
        hobbies_list[hobbies].click()

    def picture(self):
        pass

    def current_address(self, current_address: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
        element.send_keys(current_address)

    def state_and_city(self):
        pass

    def close_website(self):
        self.driver.close()