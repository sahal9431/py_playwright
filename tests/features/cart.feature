@regression
Feature: Cart Functinality

Scenario Outline: Add a product to cart and remove it
    Given user is logged in
    When user adds a product to cart
    And user opens the cart
    Then user removes the product from cart
    And cart should be empty