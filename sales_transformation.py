from pathlib import Path
import pandas as pd

# Folder containing the source files
data_folder = Path(r"data")

# Find all Excel and CSV files in the folder
input_files = list(data_folder.glob("*.xlsx")) + list(data_folder.glob("*.xls")) + list(data_folder.glob("*.csv"))

if not input_files:
    raise FileNotFoundError(f"No .xlsx, .xls, or .csv files found in {data_folder}")

all_data = []

for file_path in input_files:
    # Read file based on extension
    if file_path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)

    # Standardize column names to lowercase
    df.columns = df.columns.str.strip().str.lower()

    # Keep only Pink Morsels rows
    df = df[df["product"] == "pink morsel"].copy()

    # Clean price column and convert to float
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Convert quantity to numeric
    df["quantity"] = pd.to_numeric(df["quantity"])

    # Create Sales column
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    # Rename columns to match required output
    df.columns = ["Sales", "Date", "Region"]

    all_data.append(df)

# Combine all cleaned data
final_df = pd.concat(all_data, ignore_index=True)

# Save output file in the main project folder
output_file = Path(r"formatted_sales_data.csv")
final_df.to_csv(output_file, index=False)

print(f"Done. Output file created at: {output_file}")
print(f"Total Pink Morsels rows processed: {len(final_df)}")