import sqlite3

import pandas as pd

conn = sqlite3.connect('healthcare.db')

df = pd.read_csv('https://data.cdc.gov/resource/hn4x-zwk7.csv')

df.to_sql('health_data', conn, if_exists='replace', index=False)


conn = sqlite3.connect('healthcare.db')
query = "SELECT * FROM health_data WHERE city = 'New York'"
filtered_data = pd.read_sql_query(query, conn)
print(filtered_data)
conn.close()


conn = sqlite3.connect('healthcare.db')
query = "SELECT condition, AVG(age) FROM health_data GROUP BY condition"
avg_age_by_condition = pd.read_sql_query(query, conn)
print(avg_age_by_condition)
conn.close()


conn = sqlite3.connect('healthcare.db')
query = "SELECT * FROM health_data ORDER BY medical_expenses DESC LIMIT 5"
top_expenses = pd.read_sql_query(query, conn)
print(top_expenses)
conn.close()
