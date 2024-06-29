import sys
import pandas as pd

def convert_xlsx_to_csv(xlsx_file_path):
    # Read the .xlsx file using pandas
    df = pd.read_excel(xlsx_file_path, engine='openpyxl')

    # Define the .csv file path with the same name but with a .csv suffix
    csv_file_path = xlsx_file_path.rsplit('.', 1)[0] + '.csv'

    # Convert the DataFrame to a .csv file
    df.to_csv(csv_file_path, index=False)

    print(f"File converted and saved as: {csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_xlsx_file>")
        sys.exit(1)

    xlsx_file_path = sys.argv[1]
    convert_xlsx_to_csv(xlsx_file_path)