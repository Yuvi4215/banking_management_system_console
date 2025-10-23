"""
Cashier Instructions
====================

This file contains the operations available for Cashier role.
Cashiers handle daily money operations and customer transactions.
"""

def get_cashier_instructions():
    return """
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                    💼   CASHIER MENU - INSTRUCTIONS
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                • Welcome to the **Cashier Dashboard** — a secure and streamlined portal designed for managing daily branch operations, 
                                                including deposits, withdrawals, and transaction monitoring.

                                                • As a **Cashier**, you are responsible for assisting customers in real-time banking tasks, ensuring accuracy and 
                                                compliance.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                💰 1️⃣ DEPOSIT MONEY
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Used to deposit funds into any existing customer account.

                                                • System Prompts:
                                                    - Enter Account Number  → Customer's valid account number.
                                                    - Enter Deposit Amount  → Amount to credit to that account.

                                                • Backend Process:
                                                    - Validates the account number.
                                                    - Credits the entered amount into the customer's balance.
                                                    - Generates and records a transaction entry with:
                                                            → Type: "DEPOSIT"
                                                            → Amount, Date-Time and Cashier name.

                                                • All transactions are logged in both `transaction` and `account` files instantly.

                                                ⚠️ Ensure:
                                                - The account exists before attempting deposit.
                                                - Amount is a positive float value.
                                                - Always confirm deposit details with the customer before proceeding.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🏧 2️⃣ WITHDRAW MONEY
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Used to withdraw funds from a customer account upon proper verification.

                                                • System Prompts:
                                                    - Enter Account Number
                                                    - Enter Withdrawal Amount

                                                • Backend Process:
                                                    - Validates account existence.
                                                    - Checks if the account has sufficient balance.
                                                    - Deducts the withdrawal amount from the account.
                                                    - Generates a transaction record with:
                                                            → Type: "WITHDRAW"
                                                            → Amount, Date-Time, Cashier ID, and Remark.

                                                • Automatically updates both account balance and transaction logs.

                                                ⚠️ Ensure:
                                                - Account holder's identity is verified before withdrawal.
                                                - Enter correct account number to prevent mismatch.
                                                - Deny transaction if balance is insufficient.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🧾 3️⃣ VIEW ALL TRANSACTIONS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Displays **all transactions** recorded in the system, not limited to a specific customer.

                                                • Table Columns:
                                                    - Transaction Type
                                                    - Amount
                                                    - Date-Time
                                                    - Initiator / Target
                                                    - Remarks / Description

                                                • Fetches and formats transaction data.

                                                • Useful for reconciling daily operations and verifying recent financial activities.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🚪 4️⃣ LOGOUT
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Ends the cashier's session securely.

                                                • After logout:
                                                    - The session is invalidated.
                                                    - Access returns to the main login prompt.

                                                ⚠️ Always logout after completing shift to maintain session integrity.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                💡 TIPS FOR CASHIERS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Double-check account numbers and transaction amounts before confirmation.
                                                • For suspicious activities or large transactions, notify the Account Manager.
                                                • Maintain accurate end-of-day reconciliation using “View All Transactions”.
                                                • Avoid entering negative or non-numeric values for monetary fields.
                                                • Follow internal audit compliance for deposit/withdrawal slips.

                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""
