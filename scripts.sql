CREATE TABLE IF NOT EXISTS account (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   user_name TEXT UNIQUE,
   balance REAL,
   created_at TIMESTAMP
);


CREATE TABLE IF NOT EXISTS "transaction" (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   type TEXT,
   value REAL,
   created_at TIMESTAMP,
   account_id INTEGER,
   FOREIGN KEY (account_id) REFERENCES account(id)
);