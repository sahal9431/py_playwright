@regression
Feature: Currency Change

Scenario Outline: verify currency change
    Given user is on the home page
    When user changes currency to "<currency>"
    Then  product price should display with changed price

Examples:
|currency|
|EUR     |
|GBP     |
|USD     |
