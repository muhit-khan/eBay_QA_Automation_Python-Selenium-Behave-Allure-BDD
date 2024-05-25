Feature: Search
    Scenario: Search for a product
        Given I launch Chrome Browser
        When I open homepage
        When I search for "iPhone"
        Then I should see "iPhone" in the search results
        When I search for "Samsung"
        Then I should see "Samsung" in the search results
        When I search for "Nokia"
        Then I should see "Nokia" in the search results
        