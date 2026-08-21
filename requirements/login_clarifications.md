# Login Clarifications

1. A valid email format is defined as a standard RFC 5322-compliant email address.
2. Invalid credentials should display the specific error message: "Username and password do not match any user in this service." The message should appear in a visible error banner above the form.
3. The dashboard is identified by the inventory page at URL path "/inventory.html" and contains a visible page header with class ".title".
4. When "remember me" is not selected, the session should last only for the browser session and end when the browser is closed.
5. The login button remains disabled until both fields are filled with valid values; invalid values keep it disabled.
6. Performance metrics apply in a standard test environment with Chromium browser, no additional load, and a normal broadband connection of 25 Mbps down / 5 Mbps up.
7. Accessibility requirements are not in scope for this login requirement.
