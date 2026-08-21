# UI Application Login Requirement

## Requirement ID

REQ-SAMPLE-LOGIN-001

## Business Objective

The Sample Application must allow a user to log in using a non-empty
username and the valid password.

## Application URL

http://uitestingplayground.com/sampleapp

## Functional Requirements

### FR-001: Initial state

When the login page is opened:

- The user must be logged out.
- The status must display "User logged out."
- The login button must display "Log In".

### FR-002: Successful login

- The username must contain a non-empty value.
- The valid password is `pwd`.
- When valid credentials are submitted, the application must display:
  "Welcome, <username>!"
- The login button must change from "Log In" to "Log Out".

### FR-003: Invalid password

When a non-empty username and an incorrect password are submitted:

- Login must be rejected.
- The application must display "Invalid username/password".
- The username and password fields must be cleared.
- The login button must continue to display "Log In".

### FR-004: Empty username

When the username is empty, even if the valid password is entered:

- Login must be rejected.
- The application must display "Invalid username/password".
- The username and password fields must be cleared.

### FR-005: Logout

When a logged-in user selects "Log Out":

- The user must be logged out.
- The application must display "User logged out."
- The username and password fields must be cleared.
- The button must change back to "Log In".

## Automation Considerations

- The username and password element IDs are dynamically generated.
- Automation must not use dynamically generated IDs.
- Tests should use stable attributes, placeholders or accessible roles.
- Hard-coded waits must not be used.
