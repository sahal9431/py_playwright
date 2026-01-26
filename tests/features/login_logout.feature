@smoke
Feature: Login Functionality
Scenario Outline: Login with valid credentials
    Given user is on login page
    When user login in with email <email> and password <password>
    Then user should be navigated to home page

Examples:
  | email                      | password       |
  | leomessi107@gmail.com      | Worldcup@2022  |

@smoke
Scenario Outline: Login with invalid credentials
    Given user is on login page
    When user login in with email <email> and password <password>
    Then error message should be displayed

Examples:
  | email              | password  |
  | test@test.com      | wrong123  |
  | admin@test.com     | 123456    |
  | user@test.com      | invalid   |

@smoke
Scenario Outline: Invalid login through empty credentials
    Given user is on login page
    When user login in with email "" and password ""
    Then user should be navigated to home page

@smoke
Scenario Outline: Invalid login through empty username and valid password
    Given user is on login page
    When user login in with email "" and password "Worldcup@2022" 
    Then user should be navigated to home page

@smoke
Scenario Outline: Invalid login through valid username and empty password
    Given user is on login page
    When user login in with email "leomessi107@gmail.com" and password "" 
    Then user should be navigated to home page

@smoke
Scenario Outline: Logout
    Given user is logged in
    When user clicks on Logout
    Then user should be logged out succesfully