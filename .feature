Feature: Selenium BDD Test

    Scenario: success in submitting form data
        Given selenium opens the form website
        When script fills in the data correctly 
        And the script clicks on the submit button
        Then no error message appears and the program moves on to the next test

    Scenario: incomplete first name
        Given selenium opens the form website
        When only the first name field is filled with an empty string
        And the script clicks on the submit button
        Then the error message 'Erro encontrado: Campo "first name" inválido' appears

    Scenario: incomplete last name
        Given selenium opens the form website
        When only the last name field is filled with an empty string 
        And the script clicks on the submit button
        Then the error message 'Erro encontrado: Campo "last name" inválido' appears

    Scenario: invalid email
        Given selenium opens the form website
        When the email field is filled in without @gmail.com at the end
        And the script clicks on the submit button
        Then the error message 'Erro encontrado: Campo "email" inválido' appears

    Scenario: incomplete image field
        Given selenium opens the form website
        When only the user image field is filled with an empty string
        And the script clicks on the submit button
        Then the error message 'Erro encontrado: Campo "picture" inválido' appears
