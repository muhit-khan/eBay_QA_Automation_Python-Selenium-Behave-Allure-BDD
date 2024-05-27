from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *

# Scenario: Cart Page
@then('I should see the cart icon')
def step_impl(context):
    try:
        cart_icon = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="gh-minicart-hover"]/div/a[1]'))
        )
        assert cart_icon.is_displayed()
    except TimeoutException:
        assert False, "Cart icon is not visible"

@when('I click on cart icon')
def step_impl(context):
    try:
        cart_icon = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-minicart-hover"]/div/a[1]'))
        )
        cart_icon.click()
    except TimeoutException:
        assert False, "Cart icon is not clickable"

@then('I should see the cart page')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("cart")
        )
        cart_page = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mainContent"))
        )
        assert cart_page.is_displayed()
    except TimeoutException:
        assert False, "Cart page is not visible"

@then('I should see the Empty Cart message')
def step_impl(context):
    try:
        empty_cart_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div[3]/div/div/div/div[2]'))
        )
        assert empty_cart_message.is_displayed()
    except TimeoutException:
        assert False, "Empty Cart message is not visible"

@then('I should see the Sign In button')
def step_impl(context):
    try:
        sign_in_button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div[2]/div/div/div/div[4]/button'))
        )
        assert sign_in_button.is_displayed()
    except TimeoutException:
        assert False, "Sign In button is not visible"



# Scenario: Add to Cart
@when('I search for "Asus"')
def step_impl(context):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        search_bar.clear()
        search_bar.send_keys("Asus Motherboard")
        search_bar.submit()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search for Asus: {e}")
        raise e

@then('I should see "Asus" in the search results')
def step_impl(context):
    try:
        search_results = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".srp-controls__count-heading"))
        )
        assert "Asus" in context.driver.page_source, "Asus not found in search results"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of search results for Asus: {e}")
        raise e

@then('I should see the Add to Cart button')
def step_impl(context):
    try:
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="atcBtn_btn_1"]'))
        )
        assert add_to_cart_button.is_displayed()
    except TimeoutException:
        assert False, "Add to Cart button is not visible"

@when('I click on Add to Cart button')
def step_impl(context):
    try:
        add_to_cart_button = context.driver.find_element(By.XPATH, '//*[@id="atcBtn_btn_1"]')
        add_to_cart_button.click()
    except TimeoutException:
        assert False, "Add to Cart button is not clickable"

@then('I should see the product is added to cart')
def step_impl(context):
    try:
        cart_confirmation = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-bucket-lineitem"))
        )
        assert cart_confirmation.is_displayed()
    except TimeoutException:
        assert False, "Product is not added to cart"


# Scenario: Remove from Cart
@then('I should see the remove button')
def step_impl(context):
    try:
        remove_button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[1]/div/ul/li/div[1]/div/div/div[2]/span[2]/button'))
        )
        assert remove_button.is_displayed()
    except TimeoutException:
        assert False, "Remove button is not visible"

@when('I click on remove button')
def step_impl(context):
    try:
        remove_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[1]/div/ul/li/div[1]/div/div/div[2]/span[2]/button'))
        )
        remove_button.click()
        context.driver.refresh()
    except TimeoutException:
        assert False, "Remove button is not clickable"

@then('I should see the product is removed from cart')
def step_impl(context):
    try:
        empty_cart_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/span/span/span'))
        )
        message_text = empty_cart_message.text
        assert message_text == "Item (1)" or message_text == "Item (0)", f"Unexpected message text: {message_text}"
    except TimeoutException:
        assert False, "Product is not removed from cart"
