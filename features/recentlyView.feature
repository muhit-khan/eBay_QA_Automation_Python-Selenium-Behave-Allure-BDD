Feature: Recently Viewed Products
    Scenario: Product-1 Add to Cart 
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the search bar
        When I search for "Asus"
        Then I should see "Asus" in the search results
        And I view the product details of the seventh product
        And I should see the Add to Cart button
        When I click on Add to Cart button
        Then I should see the cart page

    Scenario: Product-2 Add to Cart 
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the search bar
        When I search for "Asus"
        Then I should see "Asus" in the search results
        And I view the product details of the seventh product
        And I should see the Add to Cart button
        When I click on Add to Cart button
        Then I should see the cart page

    Scenario: Check Recently Viewed Products Segment
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the Recently Viewed Products section
        And I should see the product-1 title
        And I should see the product-1 price
        And I should see the product-1 image

    Scenario: Check Recently Viewed Products Details
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the Recently Viewed Products section
        And I should see the product-1 title
        And I view the product page of product-1
        Then I should see the product name on the product page
        And I should see the product price on the product page
        And I should see the product description on the product page
        And I should see the product image on the product page