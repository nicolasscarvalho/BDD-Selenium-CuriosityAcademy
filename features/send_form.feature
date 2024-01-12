Feature: Selenium BDD Test

    Scenario: success in submitting form data
        Given 1 - selenium opens the form website
        When script fills in the data correctly
        Then the script clicks on the submit button and no error message appears and the program moves on to the next test

    Scenario: incomplete first name
        Given 2 - selenium opens the form website
        When only the first name field is filled with an empty string
        Then the script clicks on the submit button the error message 'Erro encontrado: Campo "first name" inválido' appears

    Scenario: incomplete last name
        Given 3 - selenium opens the form website
        When only the last name field is filled with an empty string 
        Then the script clicks on the submit button and the error message 'Erro encontrado: Campo "last name" inválido' appears

    Scenario: invalid email
        Given 4 - selenium opens the form website
        When the email field is filled in without @gmail.com at the end
        Then the script clicks on the submit button the error message 'Erro encontrado: Campo "email" inválido' appears

    Scenario: incomplete image field
        Given 5 - selenium opens the form website
        When only the user image field is filled with an empty string 
        Then the script clicks on the submit button and the error message 'Erro encontrado: Campo "picture" inválido' appears
