from behave import *
from send_form_methods import SendFormMethods

@given(u'1 - selenium opens the form website')
def step_impl(context):
    context.form = SendFormMethods()


@when(u'script fills in the data correctly')
def step_impl(context):
    assert context.form.first_name(name='abacaxi') == True
    assert context.form.last_name(last_name='laranja') == True
    assert context.form.email(email='abacaxilaranja@gmail.com') == True
    assert context.form.gender(gender=1) == True
    assert context.form.mobile(mobile='1988370591') == True
    assert context.form.date_of_birth(day=21, month=12, year=2003) == True
    assert context.form.subjects(subjects='bla bla bla') == True
    assert context.form.hobbies(hobbies=2) == True
    assert context.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\features\\steps\\user_image.png') == True
    assert context.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024') == True


@then(u'the script clicks on the submit button and no error message appears and the program moves on to the next test')
def step_impl(context):
    assert context.form.submit_and_close_website() == True


@given(u'2 - selenium opens the form website')
def step_impl(context):
    context.form = SendFormMethods()


@when(u'only the first name field is filled with an empty string')
def step_impl(context):
    assert context.form.first_name(name='') == False
    assert context.form.last_name(last_name='laranja') == True
    assert context.form.email(email='abacaxilaranja@gmail.com') == True
    assert context.form.gender(gender=1) == True
    assert context.form.mobile(mobile='1988370591') == True
    assert context.form.date_of_birth(day=21, month=12, year=2003) == True
    assert context.form.subjects(subjects='bla bla bla') == True
    assert context.form.hobbies(hobbies=2) == True
    assert context.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\features\\steps\\user_image.png') == True
    assert context.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024') == True


@then(u'the script clicks on the submit button the error message \'Erro encontrado: Campo "first name" inválido\' appears')
def step_impl(context):
    assert context.form.submit_and_close_website() == False


@given(u'3 - selenium opens the form website')
def step_impl(context):
    context.form = SendFormMethods()


@when(u'only the last name field is filled with an empty string')
def step_impl(context):
    assert context.form.first_name(name='abacaxi') == True
    assert context.form.last_name(last_name='') == False
    assert context.form.email(email='abacaxilaranja@gmail.com') == True
    assert context.form.gender(gender=1) == True
    assert context.form.mobile(mobile='1988370591') == True
    assert context.form.date_of_birth(day=21, month=12, year=2003) == True
    assert context.form.subjects(subjects='bla bla bla') == True
    assert context.form.hobbies(hobbies=2) == True
    assert context.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\features\\steps\\user_image.png') == True
    assert context.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024') == True


@then(u'the script clicks on the submit button and the error message \'Erro encontrado: Campo "last name" inválido\' appears')        
def step_impl(context):
    assert context.form.submit_and_close_website() == False


@given(u'4 - selenium opens the form website')
def step_impl(context):
    context.form = SendFormMethods()


@when(u'the email field is filled in without @gmail.com at the end')
def step_impl(context):
    assert context.form.first_name(name='abacaxi') == True
    assert context.form.last_name(last_name='laranja') == True
    assert context.form.email(email='abacaxilaranja') == False
    assert context.form.gender(gender=1) == True
    assert context.form.mobile(mobile='1988370591') == True
    assert context.form.date_of_birth(day=21, month=12, year=2003) == True
    assert context.form.subjects(subjects='bla bla bla') == True
    assert context.form.hobbies(hobbies=2) == True
    assert context.form.picture('D:\\Programacao\\BDD-Selenium-CuriosityAcademy\\features\\steps\\user_image.png') == True
    assert context.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024') == True



@then(u'the script clicks on the submit button the error message \'Erro encontrado: Campo "email" inválido\' appears')
def step_impl(context):
    assert context.form.submit_and_close_website() == True


@given(u'5 - selenium opens the form website')
def step_impl(context):
    context.form = SendFormMethods()


@when(u'only the user image field is filled with an empty string')
def step_impl(context):
    assert context.form.first_name(name='abacaxi') == True
    assert context.form.last_name(last_name='laranja') == True
    assert context.form.email(email='abacaxilaranja@gmail.com') == True
    assert context.form.gender(gender=1) == True
    assert context.form.mobile(mobile='1988370591') == True
    assert context.form.date_of_birth(day=21, month=12, year=2003) == True
    assert context.form.subjects(subjects='bla bla bla') == True
    assert context.form.hobbies(hobbies=2) == True
    assert context.form.picture('') == False
    assert context.form.current_address(current_address='Rua 04 casa n° 01, avenida 2024') == True


@then(u'the script clicks on the submit button and the error message \'Erro encontrado: Campo "picture" inválido\' appears')
def step_impl(context):
    assert context.form.submit_and_close_website() == True