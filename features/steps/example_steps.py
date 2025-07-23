from behave import given, when, then

@given('the user is on the example page')
def step_given_user_on_example_page(context):
    context.helperfunc.get('http://example.com')  # Replace with the actual URL

@when('the user performs an action')
def step_when_user_performs_action(context):
    # Example action: clicking a button
    button = context.helperfunc.find_element_by_id('exampleButton')  # Replace with actual element ID
    button.click()

@then('the user should see the result')
def step_then_user_should_see_result(context):
    result_text = context.helperfunc.find_element_by_id('result').text  # Replace with actual element ID
    assert result_text == 'Expected Result'  # Replace with the expected result text