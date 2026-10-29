# Healer Report: auth
- **Target Test File:** `testScripts/test_auth.py`
- **Status:** HEALED

## Failure Details
- **Failed Locator / Action:** `page.get_by_role("heading", name="Products")` and `page.get_by_role("heading", level=3)`
- **Error Trace:** The successful-login assertion timed out waiting for `get_by_role("heading", name="Products")` on `/inventory.html`. The other four assertions timed out waiting for `get_by_role("heading", level=3)` after login validation.

## Root Cause
- **Live DOM State:** Playwright's captured accessibility snapshots showed the inventory page exposing “Products” as text, not a heading. Login validation messages appeared inside an `alert` role, not a level-3 heading. Browser MCP tools were unavailable; the snapshots came from the actual browser pages recorded in pytest assertion failures.
- **Classification:** Locator Drift

## Fix Applied
- **Target File:** `pageObjects/auth_page.py`
- **Diff:**
```diff
-        self.error_message = page.get_by_role("heading", level=3)
-        self.inventory_heading = page.get_by_role(
-            "heading", name=inventory_heading
-        )
+        self.error_message = page.get_by_role("alert")
+        self.inventory_heading = page.get_by_text(
+            inventory_heading, exact=True
+        )
```

Assertions were not changed or weakened. The auth suite passed twice consecutively after the locator fix: 5 passed on each run.
