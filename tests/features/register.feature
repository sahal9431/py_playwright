@smoke
Feature: User registration

Scenario Outline: User able to register with valid details.
    Given user is on register page
    When user enters valid registration details
    And user submits the registration form
    Then account should be created successfully