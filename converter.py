# converter.py

import os
import sqlite3
import pandas as pd

def convert_sqlite_to_excel(sqlite_path, output_folder):
    """
    Converts all tables in a WHONET SQLite database to separate Excel files.

    Parameters:
    - sqlite_path (str): Path to the .SQLite or .db file.
    - output_folder (str): Directory where Excel files will be saved.
    """
    try:
        conn = sqlite3.connect(sqlite_path)
        cursor = conn.cursor()

        # Get all table names
        tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        if not tables:
            raise ValueError("No tables found in the database.")

        for table_name in tables:
            table = table_name[0]
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            output_path = os.path.join(output_folder, f"{table}.xlsx")
            df.to_excel(output_path, index=False)

        conn.close()

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
