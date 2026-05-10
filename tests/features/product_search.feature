@regression
Feature: Product Search Functionality

  Scenario: User can search for a product
    Given user is on the home page
    When user searches for "iPhone"
    Then search results should display products containing "iPhone"

  Scenario: User can filter search results and add to cart
    Given user is on the home page
    When user searches for "Samsung"
    And user selects the first product from search results
    Then product details page should be displayed
    And user can add product to cart from details page
