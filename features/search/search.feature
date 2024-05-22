Feature: Search
  Scenario: Test Ebay Search Functionality
    Given the user searches for "Laptop"
    Then the search results should contain "Laptop" in the title

  Scenario: Basic Search
    Given the user searches for "Laptop"
    Then the search results should be displayed

  Scenario: Search Button Functionality
    Given the user clicks the search button after entering "laptop"
    Then the search results should contain "laptop" in the title
    And the search results should be displayed

  Scenario: Test Search Result Pagination
    Given the user navigates to the search results page for "Laptop"
    Then the pagination should be displayed and functional

  Scenario: Test Filter by Condition
    Given the user navigates to the search results page for "Laptop"
    Then the user should be able to filter results by "New" condition
