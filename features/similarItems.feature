Feature: Similar Items
    Scenario: User can see similar items
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the Similar Items section
        And I should see Similar Item's title
        And I should see Similar Item's condition
        And I should see Similar Item's price

    Scenario: Visit Similar Item's page
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the Similar Items section
        And I click on the first Similar Item
        Then I should see the product name on the product page
        And I should see the product price on the product page
        And I should see the product description on the product page
        And I should see the product image on the product page