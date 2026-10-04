# Q5. Read Excel file and display result in tabular format
# Perform this program in Google Colab.
#
# If required in Google Colab, run:
# !pip install pandas openpyxl tabulate

import pandas as pd
from tabulate import tabulate

filename = "students.xlsx"

# Read Excel file
data = pd.read_excel(filename)

# Display data in tabular format
print(tabulate(data, headers="keys", tablefmt="grid", showindex=False))
