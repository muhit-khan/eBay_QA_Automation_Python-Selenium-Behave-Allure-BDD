#productPage.feature
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

    Scenario: User can see About this item
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the About this item button
        And I should see the Item specifics
        And I should see the Condition
        And I should see the Item description from the seller
        
        

    Scenario: User can see Shipping, returns, and payments
        Given I launch Chrome Browser
        When I open homepage
        And I search for "HP"
        Then I should see "HP" in the search results
        And I view the product details of the seventh product
        Then I should see the Shipping, return, and payments button
        And I should see the Shipping and handling
        And I should see the Return policy
        And I should see the Payment details