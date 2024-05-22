Feature: Miscellaneous
  Scenario: Product Listing Presence
    Given the user is on the search results page for "laptop"
    Then the user should see product listings for "laptop"

  Scenario: Product Image Display
    Given the user is on the search results page for "laptop"
    Then the product images should be displayed

  Scenario: Test Advanced Search Link
    Given the user is on the eBay homepage
    Then the "Advanced" search link should be displayed and clickable

  Scenario: Test Daily Deals Link
    Given the user is on the eBay homepage
    Then the "Daily Deals" link should be displayed and clickable

  Scenario: Test Selling on eBay Link
    Given the user is on the eBay homepage
    Then the "Sell" link should be displayed and clickable

  Scenario: Test Sign Out Button Presence
    Given the user is on the eBay homepage
    Then the "Sign out" button should not be present

  Scenario: Test Accessibility Statement Link
    Given the user is on the eBay homepage
    Then the "Accessibility" link should be displayed and clickable
