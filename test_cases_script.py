import unittest
from send_form import SendForm
from selenium import webdriver

class TestCasesScrpit(unittest.TestCase):

    def setUp(self):
        self.form = SendForm()

    def test_complete_form(self):
        try:
            self.form.first_name(name='abacaxi')
            self.form.last_name(last_name='laranja')
            self.form.email(email='abacaxilaranja@gmail.com')
            self.form.gender(gender=1)
            self.form.mobile(mobile='1988370591')
            self.form.date_of_birth(day=21, month=12, year=2003)
            self.form.subjects(subjects='bla bla bla')
            self.form.hobbies(hobbies=2)
            self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png')
            self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024')
            self.form.submit_and_close_website()
        except Exception as log:
            print(f'Erro desconhecido: {log}')

    def test_incomplete_name_field(self):
        try:
            self.form.first_name(name='')
            self.form.last_name(last_name='laranja')
            self.form.email(email='abacaxilaranja@gmail.com')
            self.form.gender(gender=1)
            self.form.mobile(mobile='1988370591')
            self.form.date_of_birth(day=21, month=12, year=2003)
            self.form.subjects(subjects='bla bla bla')
            self.form.hobbies(hobbies=2)
            self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png')
            self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024')
            self.form.submit_and_close_website()
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_lastname_field(self):
        try:
            self.form.first_name(name='abacaxi')
            self.form.last_name(last_name='')
            self.form.email(email='abacaxilaranja@gmail.com')
            self.form.gender(gender=1)
            self.form.mobile(mobile='1988370591')
            self.form.date_of_birth(day=21, month=12, year=2003)
            self.form.subjects(subjects='bla bla bla')
            self.form.hobbies(hobbies=2)
            self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png')
            self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024')
            self.form.submit_and_close_website()
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_email_field(self):
        try:
            self.form.first_name(name='abacaxi')
            self.form.last_name(last_name='laranja')
            self.form.email(email='abacaxilaranja')
            self.form.gender(gender=1)
            self.form.mobile(mobile='1988370591')
            self.form.date_of_birth(day=21, month=12, year=2003)
            self.form.subjects(subjects='bla bla bla')
            self.form.hobbies(hobbies=2)
            self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png')
            self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024')
            self.form.submit_and_close_website()
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_image_field(self):
        try:
            self.form.first_name(name='abacaxi')
            self.form.last_name(last_name='laranja')
            self.form.email(email='abacaxilaranja@gmail.com')
            self.form.gender(gender=1)
            self.form.mobile(mobile='1988370591')
            self.form.date_of_birth(day=21, month=12, year=2003)
            self.form.subjects(subjects='bla bla bla')
            self.form.hobbies(hobbies=2)
            self.form.picture('')
            self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024')
            self.form.submit_and_close_website()
        except Exception as log:
            print(f'Erro encontrado: {log}')
        

if __name__ == "__main__":
    unittest.main()