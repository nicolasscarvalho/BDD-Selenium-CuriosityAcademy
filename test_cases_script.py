import unittest
from send_form import SendForm

class TestCasesScript(unittest.TestCase):

    def setUp(self):
        self.form = SendForm()

    def test_complete_form(self):
        try:
            self.assertTrue(self.form.first_name(name='abacaxi'))
            self.assertTrue(self.form.last_name(last_name='laranja'))
            self.assertTrue(self.form.email(email='abacaxilaranja@gmail.com'))
            self.assertTrue(self.form.gender(gender=1))
            self.assertTrue(self.form.mobile(mobile='1988370591'))
            self.assertTrue(self.form.date_of_birth(day=21, month=12, year=2003))
            self.assertTrue(self.form.subjects(subjects='bla bla bla'))
            self.assertTrue(self.form.hobbies(hobbies=2))
            self.assertTrue(self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png'))
            self.assertTrue(self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024'))
            self.assertTrue(self.form.submit_and_close_website())
        except Exception as log:
            print(f'Erro desconhecido: {log}')

    def test_incomplete_name_field(self):
        try:
            self.assertTrue(self.form.first_name(name=''))
            self.assertTrue(self.form.last_name(last_name='laranja'))
            self.assertTrue(self.form.email(email='abacaxilaranja@gmail.com'))
            self.assertTrue(self.form.gender(gender=1))
            self.assertTrue(self.form.mobile(mobile='1988370591'))
            self.assertTrue(self.form.date_of_birth(day=21, month=12, year=2003))
            self.assertTrue(self.form.subjects(subjects='bla bla bla'))
            self.assertTrue(self.form.hobbies(hobbies=2))
            self.assertTrue(self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png'))
            self.assertTrue(self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024'))
            self.assertTrue(self.form.submit_and_close_website())
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_lastname_field(self):
        try:
            self.assertTrue(self.form.first_name(name='abacaxi'))
            self.assertTrue(self.form.last_name(last_name=''))
            self.assertTrue(self.form.email(email='abacaxilaranja@gmail.com'))
            self.assertTrue(self.form.gender(gender=1))
            self.assertTrue(self.form.mobile(mobile='1988370591'))
            self.assertTrue(self.form.date_of_birth(day=21, month=12, year=2003))
            self.assertTrue(self.form.subjects(subjects='bla bla bla'))
            self.assertTrue(self.form.hobbies(hobbies=2))
            self.assertTrue(self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png'))
            self.assertTrue(self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024'))
            self.assertTrue(self.form.submit_and_close_website())
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_email_field(self):
        try:
            self.assertTrue(self.form.first_name(name='abacaxi'))
            self.assertTrue(self.form.last_name(last_name='laranja'))
            self.assertTrue(self.form.email(email='abacaxilaranja'))
            self.assertTrue(self.form.gender(gender=1))
            self.assertTrue(self.form.mobile(mobile='1988370591'))
            self.assertTrue(self.form.date_of_birth(day=21, month=12, year=2003))
            self.assertTrue(self.form.subjects(subjects='bla bla bla'))
            self.assertTrue(self.form.hobbies(hobbies=2))
            self.assertTrue(self.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\user_image.png'))
            self.assertTrue(self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024'))
            self.assertTrue(self.form.submit_and_close_website())
        except Exception as log:
            print(f'Erro encontrado: {log}')

    def test_incomplete_image_field(self):
        try:
            self.assertTrue(self.form.first_name(name='abacaxi'))
            self.assertTrue(self.form.last_name(last_name='laranja'))
            self.assertTrue(self.form.email(email='abacaxilaranja@gmail.com'))
            self.assertTrue(self.form.gender(gender=1))
            self.assertTrue(self.form.mobile(mobile='1988370591'))
            self.assertTrue(self.form.date_of_birth(day=21, month=12, year=2003))
            self.assertTrue(self.form.subjects(subjects='bla bla bla'))
            self.assertTrue(self.form.hobbies(hobbies=2))
            self.assertTrue(self.form.picture(''))
            self.assertTrue(self.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024'))
            self.assertTrue(self.form.submit_and_close_website())
        except Exception as log:
            print(f'Erro encontrado: {log}')
        

if __name__ == "__main__":
    unittest.main()