DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS ledger;
DROP TABLE IF EXISTS prevision;

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
  category_name TEXT UNIQUE NOT NULL,
  account_name TEXT NOT NULL,
  category_type INTEGER NOT NULL
);

CREATE TABLE prevision (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_name TEXT NOT NULL,
  category TEXT NOT NULL,
  predicted_amount REAL NOT NULL
);

CREATE TABLE ledger (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_name TEXT NOT NULL,
  transaction_date TEXT NOT NULL,
  amount REAL NOT NULL,
  category TEXT NOT NULL,
  transaction_type INTEGER NOT NULL,
  transaction_description TEXT NOT NULL
);