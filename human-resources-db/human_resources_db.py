# -*- coding: utf-8 -*-
"""human_resources_db.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ypHZ3OMkybckKEZPmAKgENzX9OUxAtHh
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect("/content/hr.db")
conn

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables

for table in tables:
  print(table)

employee = conn.execute("SELECT * FROM employee").fetchall()
employee

employee_cols = conn.execute("PRAGMA table_info(employee)").fetchall()
employee_cols

employee_cols = [elem[1] for elem in employee_cols]
employee_cols

sales = pd.read_sql("SELECT EmployeeNumber, Department, Age, Gender FROM employee WHERE Department = 'Sales'", conn)
sales

field = pd.read_sql("SELECT EmployeeNumber, EducationField, Age, Gender FROM employee WHERE EducationField = 'Life Sciences'", conn)
field

merge = field.merge(sales, how='inner', on='EmployeeNumber')
merge