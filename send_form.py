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
        element = self.driver.find_element(By.XPATH, f'//*[@id="gender-radio-{gender}"]')
        element.click()

    def mobile(self, mobile: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="userNumber"]')
        element.send_keys(mobile)

    def date_of_birth(self, day: int, month: int, year: int):
        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        element = self.driver.find_element(By.XPATH, '//*[@id="firstName"]')
        element.send_keys(f'{day} {month_list[month] - 1} {year}')

    def subjects(self, subjects):
        element = self.driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
        element.send_keys(subjects)

    def hobbies(self, hobbies: int):
        element = self.driver.find_element(By.XPATH, f'//*[@id="hobbies-checkbox-{hobbies}"]')
        element.click()

    def picture(self, picture_path: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="uploadPicture"]')
        element.send_keys(picture_path)

    def current_address(self, current_address: str):
        element = self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
        element.send_keys(current_address)

    def state_and_city(self):
        pass

    def close_website(self):
        self.driver.close()