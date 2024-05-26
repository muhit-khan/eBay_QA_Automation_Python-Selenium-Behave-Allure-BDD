# homepage.feature
Feature: Homepage

  Scenario: Homepage Test
    Given I launch Chrome Browser
    When I open homepage
    Then the eBay logo should be displayed
    Then the search bar should be displayed
    Then the main content area should be displayed
    Then the popular categories menu should be displayed
    Then the site shifting options should be displayed
    Then the footer should be displayed