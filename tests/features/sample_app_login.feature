Feature: Sample App Login

  @REQ-SAMPLE-LOGIN-001 @TC-LOGIN-001
  Scenario: Initial logged-out state
    Given I open the Sample Application login page at "http://uitestingplayground.com/sampleapp"
    When the page finishes loading
    Then the status should state "User logged out."
    And the login button should display "Log In"
    And the username and password fields should be empty

  @REQ-SAMPLE-LOGIN-002 @TC-LOGIN-002
  Scenario: Successful login with valid credentials
    Given I am on the login page
    And the username field is populated with "alice"
    And the password field is populated with "pwd"
    When I submit the login form
    Then I should see "Welcome, alice!"
    And the login button should display "Log Out"
  # And the username and password fields should be cleared or not visible as part of logged-in UI

  @REQ-SAMPLE-LOGIN-003 @TC-LOGIN-003
  Scenario: Login rejected with invalid password
    Given I am on the login page
    And the username field is populated with "alice"
    And the password field is populated with "wrongpass"
    When I submit the login form
    Then I should see "Invalid username/password"
    And the username field should be empty
    And the password field should be empty
    And the login button should continue to display "Log In"

  @REQ-SAMPLE-LOGIN-004 @TC-LOGIN-004
  Scenario: Login rejected when username is empty
    Given I am on the login page
    And the username field is empty
    And the password field is populated with "pwd"
    When I submit the login form
    Then I should see "Invalid username/password"
    And the username field should be empty
    And the password field should be empty
    And the login button should display "Log In"

  @REQ-SAMPLE-LOGIN-005 @TC-LOGIN-005
  Scenario: Logout returns user to logged-out state
    Given I am logged in as "alice"
    When I click the "Log Out" button
    Then the user should be logged out
    And the status should state "User logged out."
    And the username and password fields should be empty
    And the login button should display "Log In"
