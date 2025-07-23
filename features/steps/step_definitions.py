from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.driver.get(context.helperfunc.get_login_url())

@when('the user enters username "{username}" and password "{password}"')
def step_when_user_enters_credentials(context, username, password):
    username_field = context.driver.find_element(By.NAME, 'username')
    password_field = context.driver.find_element(By.NAME, 'password')
    username_field.send_keys(username)
    password_field.send_keys(password)

@when('the user clicks the login button')
def step_when_user_clicks_login_button(context):
    login_button = context.driver.find_element(By.NAME, 'login')
    login_button.click()

@then('the user should see the dashboard')
def step_then_user_should_see_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'dashboard'))
    )
    assert 'Dashboard' in context.driver.title

@then('the user should see an error message "{message}"')
def step_then_user_should_see_error_message(context, message):
    error_message = context.driver.find_element(By.CLASS_NAME, 'error')
    assert error_message.text == message