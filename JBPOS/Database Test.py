import sqlite3
conn = sqlite3.connect('tester.db')
cursor = conn.cursor()
table = """ CREATE TABLE IF NOT EXISTS CUSTOMER (
            First_Name  TEXT NOT NULL,
            Last_Name   TEXT NOT NULL,
            Phone       TEXT NOT NULL,
            Address     TEXT,
            Customer_ID INT NOT NULL
); """
cursor.execute(table)
table_2 = """ CREATE TABLE IF NOT EXISTS DOGS
              Dog_Name TEXT NOT NULL,
              Breed TEXT NOT NULL,
              Weight INT
              LastVax TEXT NOT NULL,
              VetName TEXT NOT NULL
              Customer_ID INT NOT NULL
              FOREIGN KEY(Customer_ID) REFERENCES CUSTOMER(Customer_ID)
);"""
cursor.execute(table_2)
table_3 = """ CREATE TABLE IF NOT EXISTS TRANSACTIONS
"""
conn.close()


