DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS ledger;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  starting_balance REAL
);

--type is 0 or 1 and corresponds to outcome and income
--predicted_amount is the amount that i want to allocate
-- to that category for the current year
CREATE TABLE category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_category TEXT UNIQUE NOT NULL,
  type_category INTEGER NOT NULL,
  predicted_amount REAL NOT NULL
);

CREATE TABLE ledger (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_id INTEGER NOT NULL,
  date_transaction TEXT NOT NULL,
  amount REAL NOT NULL,
  category TEXT NOT NULL,
  type_transaction INTEGER NOT NULL,
  description_transaction TEXT NOT NULL
);