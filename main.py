# Downloading files from Kaggle (default location: C:\Users\<user name>>\.cache\kagglehub\datasets
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("muhammadatiflatif/coca-cola-stock-data-over-100-years-of-trading")
#
# print("Path to dataset files:", path)
#######################################################################################################################
# # converting .CSV file into sqlite database
# import sqlite3
# import csv
#
# csv_file = 'KO_1919-09-06_2025-05-12.csv'
# table_name = 'CocaCola_stock_date'
#
# # Otwórz plik i wczytaj dane
# with open(csv_file, newline='', encoding='utf-8') as f:
#     reader = list(csv.reader(f))
#     second_row = reader[0]  # Using second line of .csv file as our colum headers
#     data_rows = reader[2:]  # Data starts from third row
#
# # Prepare correct column names
# columns = [f'"{col.strip().replace(" ", "_")}" TEXT' for col in second_row]
# columns_str = ', '.join(columns)
#
# # SQLite database connection
# conn = sqlite3.connect('project_database.db')
# cursor = conn.cursor()
#
# # Table creation
# cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
# cursor.execute(f'CREATE TABLE {table_name} ({columns_str})')
#
# # WData insertion
# placeholders = ', '.join('?' * len(second_row))
# cursor.executemany(
#     f'INSERT INTO {table_name} VALUES ({placeholders})',
#     data_rows
# )
#
# conn.commit()
# conn.close()
# print(f"Table '{table_name}' has been created.")
