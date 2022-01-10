sql_user_transactions_date_range = "SELECT transaction_date,amount,category,transaction_type,transaction_description FROM ledger WHERE account_name=? AND transaction_date BETWEEN ? AND ?"
sql_user_transactions = "SELECT transaction_date,amount,category,transaction_type,transaction_description FROM ledger WHERE account_name=?"
sql_user_info = "SELECT username,starting_balance FROM user where username=?"
sql_user_previsions = (
    "SELECT category,predicted_amount FROM prevision where account_name=?"
)
sql_user_categories = (
    "SELECT category_name,account_name,category_type FROM category where account_name=?"
)
sql_set_user_balance = "UPDATE user SET starting_balance=? WHERE username=?"
sql_insert_transaction = ""
