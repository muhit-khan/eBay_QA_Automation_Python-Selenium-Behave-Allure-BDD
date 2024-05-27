Feature: Customer also bought
    Scenario: User can see Customer also bought items
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the Customer also boughts section
        And I should see Customer also bought item's condition
        And I should see Customer also bought item's price
        And I should see Customer also bought item's title

    Scenario: Visit Customer also bought's page
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the Customer also boughts section
        And I click on the first Customer also boughts Item
        Then I should see the product name on the product page
        And I should see the product price on the product page
        And I should see the product description on the product page
        And I should see the product image on the product page