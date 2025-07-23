Feature: Example Feature

  Scenario: Verify the title of the homepage
    Given I open the homepage
    Then I should see the title "Welcome to the Example Page"

  Scenario: Check the presence of a specific element
    Given I open the homepage
    Then I should see the element with id "example-element"