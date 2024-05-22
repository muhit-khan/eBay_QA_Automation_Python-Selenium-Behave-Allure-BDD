Feature: Homepage
  Scenario: Homepage Load Test
    Given the user is on the eBay homepage
    Then the eBay logo should be displayed
    And the search bar should be displayed
    And the main content area should be displayed

  Scenario: Test Ebay Home Page Title
    Given the user is on the eBay homepage
    Then the title should contain "eBay"
