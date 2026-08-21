Q-001 | Related requirement: FR-2 (Successful login)
Question: Are `alice`/`pwd` guaranteed test credentials, or should a test credentials store be provided?
Why required: Tests depend on known valid credentials.
Testing impact: Without stable credentials, successful login scenarios cannot be validated.
Priority: High

Q-002 | Related requirement: FR-2 (post-login UI)
Question: After successful login, should username/password inputs be cleared or hidden (which behavior is authoritative)?
Why required: Test assertions differ between "inputs cleared" vs "not visible".
Testing impact: Clarifies expected assertions for success scenario.
Priority: Medium

Q-003 | Related requirement: Performance/Timing
Question: What is the maximum acceptable page load time or explicit wait threshold for tests to use?
Why required: To set reliable timeouts and avoid flakiness.
Testing impact: Affects DEFAULT_TIMEOUT and wait strategies.
Priority: Medium

Q-004 | Related requirement: Error messaging
Question: Is the error message text for failed login exactly "Invalid username/password" or are variations allowed?
Why required: Tests currently perform substring or exact matching; clarity avoids brittle asserts.
Testing impact: Determines whether to use exact or substring matches.
Priority: Medium

Q-005 | Related requirement: Environment
Question: Is Chromium required for CI runs, or is system Chrome acceptable (helps work around sandbox issues)?
Why required: Test environment earlier showed Playwright bundle launch issues on macOS sandbox.
Testing impact: Affects fixture configuration and CI environment setup.
Priority: High
# Clarification Questions

- Question ID: Q6
  - Related requirement: Non-functional requirements
  - Question: What are the expected test conditions for the page load and login process performance criteria, including browser, environment, and network definitions?
  - Why clarification is required: Performance criteria require a controlled baseline to test reliably.
  - Testing impact: Needed to validate non-functional requirements and avoid false failures.
  - Priority: Medium

- Question ID: Q7
  - Related requirement: Accessibility and security
  - Question: Are there any additional accessibility or security requirements for the login page, such as keyboard navigation, screen reader support, password masking, or brute-force protections?
  - Why clarification is required: These aspects are not documented but are common for login flows.
  - Testing impact: Needed to identify additional critical test coverage.
  - Priority: Low

