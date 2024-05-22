Feature: Navigation
  Scenario: Test Ebay Navigation Bar Links
    Given the user is on the eBay homepage
    Then the navigation bar should have "Electronics", "Saved", and "Motors" links

  Scenario: Test Ebay Community
    Given the user is on the eBay homepage
    Then the user should be able to navigate to the "eBay Community" page

  Scenario: Logo Link Test
    Given the user is on the eBay homepage
    Then the eBay logo should link to the homepage

  Scenario: Category Navigation
    Given the user is on the eBay homepage
    Then the user should be able to navigate to the "Electronics" category

  Scenario: Sub-category Navigation
    Given the user is on the "Electronics" category page
    Then the user should be able to navigate to the "Cell Phones & Accessories" sub-category
