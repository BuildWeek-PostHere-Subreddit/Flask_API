"""Run this file to create a sqlite3 database based on the CSV file"""

import pandas as pd
import sqlite3


# Use pandas to import CSV as a dataframe
df = pd.read_csv('subreddit_info.csv')
print(f'The shape of the dataset is {df.shape}')

# Check for missing values
nulls = 0
for i in range(len(df.columns)):
    col_nulls = df.isnull().sum()[i]
    nulls += col_nulls
    if col_nulls > 0:
        print(f'Column {df.columns[i]} has {nulls} missing values.')
if nulls == 0:
    print('This dataset has no missing values!')

# Create a database in sqlite3
conn = sqlite3.connect('subreddit_db.sqlite3')

# Convert dataframe to a table in the new database
df.to_sql('subreddit', con=conn)

# Confirm that the conversion worked
print('Testing to see if the converstion to sqlite3 worked:')
curs = conn.cursor()

query = 'SELECT COUNT(*) FROM subreddit;'
output = curs.execute(query).fetchone()
amount = output[0]
print(f'After converting to sqlite, the dataset contains {amount} rows.')
