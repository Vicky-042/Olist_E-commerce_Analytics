from pathlib import Path
import pandas as pd

#Folder conaining orginal csv files
raw_folder = Path(r"C:\Users\VIGNESH\OneDrive\Desktop\olist-ecommerce-analytics\data\raw")
csv_files = sorted(raw_folder.glob("*.csv"))

if not csv_files:
    print(f"no csv files in:{raw_folder}")
else:
    print(f"Found {len(csv_files)} CSV files in: {raw_folder}")

for file_path in csv_files:
    print(f"\n{'=' * 70}")
    print(f"File: {file_path.name}")

    try:
        #Read the file to count rows and identify columns.
        #The raw file is only read; it is not modified.
        data = pd.read_csv(file_path, encoding="utf-8")


        print(f"Rows: {len(data):,}")
        print(f"Columns: ({len(data.columns)}):")
        print(list(data.columns))
        print("First 2 rows:")
        print(data.head(2).to_string(index=False))

    except Exception as error:
        print(f"Could not read this file: {error}")
    