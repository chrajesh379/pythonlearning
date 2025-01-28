import pandas as pd
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.read_csv(r"C:\Rajesh\OneDrive\Rajesh\Github_Code\pythonlearning\ventia_misaligned__1504.csv",sep=',', quotechar='"')
#print(df)
#print(df["transaction_description"])
#print(df["vendor_country"])
print(df["po_number"])