Feature: Footer
  Scenario: Test Ebay Footer Links
    Given the user is on the eBay homepage
    When the user scrolls to the bottom of the page
    Then the footer should contain the "eBay Community" link

  Scenario: Footer Links Presence
    Given the user is on the eBay homepage
    When the user scrolls to the bottom of the page
    Then the footer should have links
