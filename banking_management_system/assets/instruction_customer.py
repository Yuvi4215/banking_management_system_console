"""
Customer Instructions
=====================

This file contains the operations available for Customer role.
Customers can view their account, manage their funds, and check transaction history.
"""

def get_customer_instructions():
    return """
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                    🧍   CUSTOMER MENU - INSTRUCTIONS
                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                • Welcome to your **Customer Dashboard** — your secure banking portal to manage funds, view balances, and monitor all 
                                                transactions.
                                                • Each option corresponds to a real-time operation connected to your digital bank account.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                📘 1️⃣ VIEW ACCOUNT DETAILS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Displays all your key account details fetched securely from the system:
                                                    - Username
                                                    - Password
                                                    - Role (CUSTOMER)
                                                    - Account Number
                                                    - Current Balance

                                                • The information is fetched using your encrypted ID from the database, ensuring data privacy.
                                                • Ideal for verifying your current balance or confirming your registered account details.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                💸 2️⃣ TRANSFER MONEY
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Securely transfer money to another customer's account within the same banking system.

                                                • You will be prompted to enter:
                                                    - Recipient's Account Number
                                                    - Amount to Transfer

                                                • The system will automatically:
                                                    - Validate that the recipient account exists.
                                                    - Ensure sufficient funds in your balance.
                                                    - Update both sender and receiver account balances.
                                                    - Record the transaction in both users' transaction logs with timestamps and remarks.

                                                • Transactions are instant and reflected across files.

                                                ⚠️ Note:
                                                Enter valid numeric inputs for account numbers and amounts.
                                                Transfers cannot be undone once processed.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🧾 3️⃣ VIEW TRANSACTION HISTORY
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • View a complete list of all your past transactions — fetched directly from the transaction database.

                                                • Each record shows:
                                                    - Transaction Type  (DEPOSIT / TRANSFER SENT / TRANSFER RECEIVED)
                                                    - Transaction Amount
                                                    - Transaction Date and Time
                                                    - Remark or Description

                                                • Helps you keep track of your spending and deposits with a clear, timestamped history.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🧾 4️⃣ RECEIVE MONEY THROUGH UPI
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • This feature allows you to **receive funds instantly via UPI** within your banking system.

                                                • You will be asked to:
                                                    - Enter the amount you expect to receive.
                                                    - A unique **QR Code** will be generated for the transaction.
                                                    - The sender can scan this QR code to complete payment.

                                                • Once the sender confirms payment:
                                                    - Do confirm Transaction done/failed.
                                                    - Your account balance is updated automatically.
                                                    - A success message will confirm the credit to your account.
                                                    - The transaction is recorded in your log with a timestamp.

                                                ⚠️ If the transaction fails or is canceled:
                                                - No money will be credited.

                                                💡 Tips for UPI Transactions:
                                                - Ensure stable internet connection.
                                                - Verify the QR code matches your account before sharing.
                                                - Always confirm transaction success before closing the screen.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                🚪 5️⃣ LOGOUT
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Securely exit your customer session.
                                                • Recommended after completing transactions to prevent unauthorized access.

                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                💡 TIPS FOR CUSTOMERS
                                                ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                • Always double-check recipient account numbers before confirming a transfer.
                                                • Do not share your password or encrypted ID with anyone.
                                                • Review your transaction history frequently to ensure accuracy.
                                                • Maintain a sufficient balance for future transfers and checkbook requests.

                                                ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

