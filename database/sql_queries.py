CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FISRT_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

CREATE_BAN_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban
(
    ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    COUNT INTEGER
)
"""

INSERT_OR_UPDATE_BAN_USER_QUERY = """
INSERT INTO ban (TELEGRAM_ID, COUNT) 
VALUES (?, 1)
ON CONFLICT(TELEGRAM_ID) DO UPDATE SET COUNT = COUNT + 1
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban WHERE TELEGRAM_ID = ?
"""

BAN_USER_THRESHOLD = 3

SELECT_ALL_USERS_QUERY = """
SELECT * FROM telegram_users
"""

SELECT_POTENTIAL_BANS_QUERY = """
SELECT tu.*, bu.count AS ban_count
FROM telegram_users tu
LEFT JOIN ban_users bu ON tu.telegram_id = bu.telegram_id
"""

CREATE_WALLET_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wallet
(
    ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    BALANCE INTEGER DEFAULT 0,
    UNIQUE (TELEGRAM_ID)
)
"""

INSERT_WALLET_QUERY = """
INSERT OR IGNORE INTO wallet VALUES (?, ?, ?)
"""

SELECT_WALLET_BALANCE_QUERY = """
SELECT BALANCE FROM wallet WHERE TELEGRAM_ID = ?
"""

UPDATE_WALLET_BALANCE_QUERY = """
UPDATE wallet SET BALANCE = BALANCE + ? WHERE TELEGRAM_ID = ?
"""