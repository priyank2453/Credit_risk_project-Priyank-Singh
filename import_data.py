import pandas as pd
from sqlalchemy import create_engine

# Load your CSV
df = pd.read_csv("C:/Users/VICTUS/Downloads/archive (3)/Loan_Default.csv")  # <-- change this to your actual file path

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:123456@localhost/credit_risk")  # <-- change YOUR_PASSWORD

# Load it into a table
df.to_sql("loan_data_raw", con=engine, if_exists="replace", index=False)

print("Done. Rows loaded:", len(df))