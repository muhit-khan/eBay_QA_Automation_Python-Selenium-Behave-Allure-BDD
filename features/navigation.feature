#navigation.feature
Feature: Navigation
    Scenario: Test Ebay Navigation Bar Links
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the Saved in navigation bar
        And I should see the Electronics in navigation bar
        And I should see the Motors in navigation bar
        And I should see the Fashion in navigation bar
        And I should see the Collectibles and Art in navigation bar
        And I should see the Sports in navigation bar
        And I should see the Health & Beauty in navigation bar
        And I should see the Industrial equipment in navigation bar
        And I should see the Home & Garden in navigation bar
        And I should see the Deals in navigation bar
        And I should see the Sell in navigation bar