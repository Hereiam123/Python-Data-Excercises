import pandas as pd

# Read in a CSV
print(pd.read_csv('CSV Content/example.csv'))

# Write to a CSV
df = pd.read_csv('CSV Content/example.csv')
df.to_csv('CSV Content/My_output.csv', index=False)

print(pd.read_csv('CSV Content/My_output.csv'))

# Read in Excel File by Sheet
print(pd.read_excel('CSV Content/Excel_Sample.xlsx', sheet_name="Sheet1"))
df = pd.read_excel('CSV Content/Excel_Sample.xlsx', sheet_name="Sheet1")
df.to_excel('CSV Content/Excel_Sample2.xlsx', sheet_name="NewSheet")
