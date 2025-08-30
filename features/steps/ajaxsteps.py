from behave import given, when, then
from pages.home_page import HomePage
from pages.ajax_form_page import AjaxFormPage
from utils.config import BASE_URL

@given('the user navigates to Url')
def step_navigate_to_url(context):
    context.browser.get(BASE_URL)
    context.home_page = HomePage(context.browser)

@when('the user clicks on "Ajax Form Submit"')
def step_click_on_menu(context):
    context.home_page.click_login()  # Replace with actual method for clicking the menu

@when('the user submits the form with name "<name>" and comment "<comment>"')
def step_fill_ajax_form(context, name, comment):
    context.ajax_form_page = AjaxFormPage(context.browser)
    context.ajax_form_page.enter_name(name)
    context.ajax_form_page.enter_comment(comment)
    context.ajax_form_page.click_submit()

@then('the user should see the message "<expected_text>"')
def step_assert_success_message(context, expected_text):
    message = context.ajax_form_page.get_success_message()
    assert expected_text in message