@smoke
Feature: User registration with data-driven testing

Scenario Outline: User able to register with valid details
    Given user is on register page
    When user registers with "<firstName>" "<lastName>" and "<newsletter>"
    Then account should be created successfully

Examples: Valid registration data
    | firstName | lastName | newsletter |
    | John      | Doe      | Yes        |
    | Jane      | Smith    | No         |
    | Mike      | Wilson   | Yes        |
    | Sarah     | Johnson  | Yes        |