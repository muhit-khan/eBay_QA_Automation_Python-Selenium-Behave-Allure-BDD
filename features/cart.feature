Feature: Cart
    
    Scenario: Cart Page
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the cart icon
        When I click on cart icon
        Then I should see the cart page
        Then I should see the Empty Cart message
        Then I should see the Sign In button
    
    Scenario: Add to Cart
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the search bar
        When I search for "Asus"
        Then I should see "Asus" in the search results
        And I view the product details of the seventh product
        And I should see the Add to Cart button
        When I click on Add to Cart button
        Then I should see the cart page
        Then I should see the product is added to cart

    Scenario: Remove from Cart
        Given I launch Chrome Browser
        When I open homepage
        Then I should see the search bar
        When I search for "Asus"
        Then I should see "Asus" in the search results
        And I view the product details of the seventh product
        And I should see the Add to Cart button
        When I click on Add to Cart button
        Then I should see the cart page
        Then I should see the product is added to cart
        Then I should see the remove button
        When I click on remove button
        Then I should see the product is removed from cart
        When I click on remove button
        Then I should see the Empty Cart message