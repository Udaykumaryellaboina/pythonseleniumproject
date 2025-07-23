# features/steps/homepage_steps.py
from behave import given, then
from selenium import webdriver

@given(u'I open the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://your-homepage-url.com')

@then(u'I should see the title "Welcome to the Example Page"')
def step_impl(context):
    assert context.browser.title == "Welcome to the Example Page"

@then(u'I should see the element with id "example-element"')
def step_impl(context):
    element = context.browser.find_element("id", "example-element")
    assert element is not None