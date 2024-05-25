Feature: Product Page
    Scenario: User can view product details
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the product name on the product page
        And I should see the product price on the product page
        And I should see the product description on the product page
        And I should see the product image on the product page