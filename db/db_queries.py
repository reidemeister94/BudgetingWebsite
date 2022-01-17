get_user_transactions_date_range = (
    "SELECT * FROM ledger WHERE account_name=? AND transaction_date BETWEEN ? AND ?"
)
get_user_transactions = "SELECT * FROM ledger WHERE account_name=?"
get_user_info = "SELECT id,username,starting_balance FROM user where username=?"
get_user_previsions = "SELECT * FROM prevision where account_name=?"
get_user_categories = "SELECT * FROM category where account_name=?"

check_transaction_in_db = "SELECT * FROM ledger WHERE id=? AND account_name=?"


set_user_balance = "UPDATE user SET starting_balance=? WHERE username=?"


insert_user = "INSERT INTO user (username,password,starting_balance) VALUES (?,?,?)"
insert_transaction = "INSERT INTO ledger (account_name,transaction_date,amount,category,transaction_type,transaction_description) VALUES (?,?,?,?,?,?)"
insert_category = (
    "INSERT INTO category (category_name,account_name,category_type) VALUES (?,?,?)"
)
insert_prevision = (
    "INSERT INTO prevision (category,account_name,predicted_amount) VALUES (?,?,?)"
)

update_starting_balance = "UPDATE user SET starting_balance=? WHERE username=?"
update_transaction = "UPDATE ledger SET transaction_date=?,amount=?,category=?,transaction_type=?,transaction_description=? WHERE id=?"
update_category = "UPDATE category SET category_name=?,category_type=? WHERE id=?"
update_prevision = "UPDATE prevision SET category=?,predicted_amount=? WHERE id=?"


delete_transaction = "DELETE FROM ledger WHERE id=?"
delete_category = "DELETE FROM category WHERE id=?"
delete_prevision = "DELETE FROM prevision WHERE id=?"
