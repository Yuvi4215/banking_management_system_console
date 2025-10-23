"""
Account Manager Instructions
============================

This file contains the operations available for Account Manager role.
Account Managers oversee customer onboarding and account maintenance.
"""

def get_account_manager_instructions():
    return """
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                    🧾 ACCOUNT MANAGER MENU - INSTRUCTIONS
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                • Welcome to the **Account Manager Dashboard** — this module allows managers to oversee all customer accounts, 
                                                create new profiles, manage existing records, and maintain operational integrity.

                                                •  As an **Account Manager**, you have administrative control over account registration, validation, 
                                                and removal processes.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🧍 1️⃣ CREATE NEW CUSTOMER ACCOUNT
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Used to register a new customer and open their first bank account.

                                                • System Prompts:
                                                    - Username (First 5 characters considered)
                                                    - Password (First 5 characters considered)
                                                    - Full Name (No digits allowed, max length 15)
                                                    - Email (Must end with @gmail.com)
                                                    - Phone Number (Digits only, exactly 10 characters)
                                                    - Address (Max length 50)
                                                    - Initial Balance (Positive numeric value)

                                                • Backend Process:
                                                    - Checks if username is already taken.
                                                    - Validates each input for format and logical correctness.
                                                    - Generates a **unique encrypted account number**, ensuring:
                                                            → Not already in `identifier_db`.
                                                            → Not duplicated in `account_db` or `customer_db`.
                                                    - Saves records in:
                                                            1️⃣ `identifier_db`
                                                            2️⃣ `customer_db`
                                                            3️⃣ `account_db`
                                                            4️⃣ `transaction_db`
                                                    - Displays the generated account number upon successful creation.

                                                ⚠️ Validation Summary:
                                                    - Full Name → must not contain digits.
                                                    - Email → must end with “@gmail.com”.
                                                    - Phone → must contain only digits.
                                                    - Balance → must be a positive float.

                                                💡 Tip:
                                                Always double-check details before creating an account — once created, the encrypted ID links across all system databases.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                📋 2️⃣ VIEW ALL CUSTOMERS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Displays every registered customer in the system in pretty table format.

                                                • Columns Displayed:
                                                    - ID (Encrypted)
                                                    - Username
                                                    - Full Name
                                                    - Email
                                                    - Phone
                                                    - Address
                                                    - Account Number

                                                • Backend Process:
                                                    - Fetches customer list.
                                                    - Formats the result into a table using `create_table()` for neat CLI visualization.

                                                ✅ Use this feature to verify existing accounts and customer details quickly.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🗑️ 3️⃣ DELETE CUSTOMER ACCOUNT
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Used to delete a customer account permanently.

                                                • System Prompts:
                                                    - Enter Account Number
                                                    - Confirm Deletion (y/n)

                                                • Backend Process:
                                                    - Verifies if entered account number exists.
                                                    - If found, removes all linked entries (identifier, account, and customer data).
                                                    - Uses `AccountService.deleteCustomer()` for cleanup.
                                                    - Displays confirmation upon success.

                                                ⚠️ Caution:
                                                Deleting a customer removes their entire account and transaction history — this action is irreversible.

                                                💡 Tip:
                                                Perform deletions only after verifying identity and obtaining proper authorization.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🚪 4️⃣ LOGOUT
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Safely exits the manager dashboard and returns to the login screen.

                                                • Ensures:
                                                    - Session is securely terminated.
                                                    - No lingering data or cached credentials remain active.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                💡 BEST PRACTICES FOR ACCOUNT MANAGERS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Always validate customer data thoroughly during registration.
                                                • Use clear naming conventions for usernames (first 5 characters rule).
                                                • Verify balances and account info before deletion.
                                                • For duplicate or suspicious entries, coordinate with system admin.
                                                • Maintain confidentiality — never share customer details outside official processes.

                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""
