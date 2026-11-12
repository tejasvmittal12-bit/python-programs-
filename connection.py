import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened database successfully')

import pandas as pd
tables = pd.read_sql_query("""SELECT *
FROM sqlite_master WHERE type='table';""", conn)
tables