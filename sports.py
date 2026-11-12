# ============================================================
# SQL Constraints
# Activity: Sports Team Player Database
# ============================================================
 
# ---- PART 1: Create the Table with Constraints ----
# SQL constraints are rules written inside CREATE TABLE.
# They control what data each column is allowed to store.
# If a row breaks a constraint, the insert is rejected.
# Constraints keep the database accurate and reliable.
 
import sqlite3
import pandas as pd
 
conn = sqlite3.connect('sports_team.db')
 
conn.execute("DROP TABLE IF EXISTS Player;")
 
conn.execute("""
CREATE TABLE Player (
    Player_Id     INTEGER PRIMARY KEY,
    Player_Name   TEXT    NOT NULL UNIQUE,
    Team_Name     TEXT    NOT NULL,
    Jersey_Number INTEGER,
    Is_Captain    TEXT    DEFAULT 'No'
);
""")
conn.commit()
print("Table created successfully!")
 
# ---- PART 2: INSERT — Adding Rows to the Table ----
# INSERT INTO adds one row at a time.
# Every NOT NULL column must receive a value.
# Columns with a DEFAULT can be left out — the default fills in.
# conn.commit() saves all inserts permanently.
 
conn.execute("INSERT INTO Player VALUES (1, 'Aarav', 'Tigers', 7, 'Yes');")
conn.execute("INSERT INTO Player VALUES (2, 'Diya', 'Tigers', 10, 'No');")
conn.execute("INSERT INTO Player VALUES (3, 'Kabir', 'Lions', 9, 'Yes');")
conn.execute("INSERT INTO Player VALUES (4, 'Meera', 'Lions', 4, 'No');")
conn.execute("INSERT INTO Player VALUES (5, 'Riya', 'Eagles', 11, 'No');")
conn.execute("INSERT INTO Player (Player_Id, Player_Name, Team_Name) VALUES (6, 'Arjun', 'Eagles');")
conn.commit()
print("Rows inserted successfully!")
 
players = pd.read_sql("SELECT * FROM Player;", conn)
print(players)
 
# ---- PART 3: PRIMARY KEY in Action ----
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same Player_Id.
# The column also cannot be NULL.
# Trying to insert a duplicate PRIMARY KEY raises an error.
 
print("\n--- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO Player VALUES (1, 'Zoya', 'Sharks', 8, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Player_Id 1 already belongs to Aarav — PRIMARY KEY must be unique.")
 
# ---- PART 4: NOT NULL and UNIQUE in Action ----
# NOT NULL means the column cannot be left without a value.
# UNIQUE means no two rows can share the same value in that column.
# Player_Name is both NOT NULL and UNIQUE.
 
print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO Player VALUES (7, 'Anaya', NULL, 6, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Team_Name is NOT NULL — every player must have a team name.")
 
print("\n--- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO Player VALUES (8, 'Aarav', 'Sharks', 12, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Player_Name is UNIQUE — 'Aarav' is already in the table.")
 
# ---- PART 5: DEFAULT in Action ----
# DEFAULT sets an automatic value when no value is provided.
# Arjun was inserted without Is_Captain.
# The DEFAULT 'No' was applied automatically.
 
print("\n--- DEFAULT value check for Arjun ---")
arjun = pd.read_sql("""SELECT Player_Name, Team_Name, Is_Captain
    FROM Player
    WHERE Player_Name == 'Arjun';""", conn)
 
print(arjun)
print("Is_Captain was not given — DEFAULT 'No' was used automatically.")
 
# ---- PART 6: NULL Values ----
# NULL means no value is stored — it is not zero and not an empty string.
# A column without NOT NULL can store NULL.
# Use IS NULL to find rows where data is missing.
# Use IS NOT NULL to find rows where data was provided.
 
print("\n--- NULL in the Jersey_Number column ---")
all_players = pd.read_sql("""SELECT Player_Name, Team_Name, Jersey_Number
    FROM Player;""", conn)
 
print(all_players)
 
missing = pd.read_sql("""SELECT Player_Name FROM Player
    WHERE Jersey_Number IS NULL;""", conn)
 
print("Players with no jersey number:")
print(missing)
 
has_data = pd.read_sql("""SELECT Player_Name, Jersey_Number FROM Player
    WHERE Jersey_Number IS NOT NULL;""", conn)
 
print("Players with jersey numbers:")
print(has_data)
 
conn.close()
