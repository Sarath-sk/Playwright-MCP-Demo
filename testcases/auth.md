# Test Plan: auth
**Target URL:** https://www.saucedemo.com
**Date:** 2026-10-29

## Preconditions
- The SauceDemo login page is available in a browser.
- Use the publicly provided SauceDemo test accounts and credentials specified in each scenario.
- Start each scenario from a fresh login page.

## Scenarios
### Scenario 1.1 — Successful login with standard_user
- **Type:** Positive
- **Priority:** P0
- **Preconditions:** Login page is displayed.
- **Steps:**
  1. Enter `standard_user` in the Username field — expected: the username is entered.
  2. Enter `secret_sauce` in the Password field — expected: the password is entered.
  3. Select Login — expected: the inventory page opens.
- **Assertions:**
  - The inventory page is displayed with the Products heading.
  - The browser URL is `https://www.saucedemo.com/inventory.html`.

### Scenario 1.2 — Locked out user validation
- **Type:** Negative
- **Priority:** P1
- **Preconditions:** Login page is displayed.
- **Steps:**
  1. Enter `locked_out_user` in the Username field — expected: the username is entered.
  2. Enter `secret_sauce` in the Password field — expected: the password is entered.
  3. Select Login — expected: login is rejected and an error message is displayed.
- **Assertions:**
  - The error message reads `Epic sadface: Sorry, this user has been locked out.`
  - The login page remains displayed.

### Scenario 1.3 — Empty username submission
- **Type:** Corner
- **Priority:** P1
- **Preconditions:** Login page is displayed; both fields are empty.
- **Steps:**
  1. Select Login without entering a username or password — expected: submission is rejected and a validation error is displayed.
- **Assertions:**
  - The error message reads `Epic sadface: Username is required`.
  - The login page remains displayed.

### Scenario 1.4 — Empty password submission
- **Type:** Corner
- **Priority:** P1
- **Preconditions:** Login page is displayed.
- **Steps:**
  1. Enter `standard_user` in the Username field — expected: the username is entered.
  2. Leave the Password field empty.
  3. Select Login — expected: submission is rejected and a validation error is displayed.
- **Assertions:**
  - The error message reads `Epic sadface: Password is required`.
  - The login page remains displayed.

### Scenario 1.5 — Invalid credentials
- **Type:** Negative
- **Priority:** P1
- **Preconditions:** Login page is displayed.
- **Steps:**
  1. Enter an invalid username and password — expected: both values are entered.
  2. Select Login — expected: login is rejected and an error message is displayed.
- **Assertions:**
  - The error message reads `Epic sadface: Username and password do not match any user in this service`.
  - The login page remains displayed.
