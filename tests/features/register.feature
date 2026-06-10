@smoke
Feature: User registration with data-driven testing

Scenario Outline: User able to register with valid details
    Given user is on register page
    When user enters "<firstName>" as first name
    And user enters "<lastName>" as last name
    And user enters "<email>" as email
    And user enters "<telephone>" as telephone
    And user enters "<password>" as password
    And user enters "<confirmPassword>" as confirm password
    And user selects newsletter "<newsletter>"
    And user agrees to terms and conditions
    And user submits the registration form
    Then account should be created successfully

Examples: Valid registration data
    | firstName | lastName | email                    | telephone  | password   | confirmPassword | newsletter |
    | John      | Doe      | john.doe@example.com     | 9876543210 | Test@1234  | Test@1234       | Yes        |
    | Jane      | Smith    | jane.smith@example.com   | 9123456789 | Pass@1234  | Pass@1234       | No         |
    | Mike      | Wilson   | mike.wilson@example.com  | 9988776655 | Secure@1234| Secure@1234     | Yes        |
    | Sarah     | Johnson  | sarah.j@example.com      | 9876123456 | Strong@2024| Strong@2024     | Yes        |