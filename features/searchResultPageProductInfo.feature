Feature: Search Product Information
    Scenario: Search for a product
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the search bar
        When I search for "Dell"
        Then I should see "Dell" in the search results
        Then I should see the product name
        Then I should see the price of the product
        Then I should see the condition of the product
        Then I should see the product image