
import pandas as pd

def parse_log(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.txt'):
            df = pd.read_csv(file_path, sep=';', names=["Time", "ID", "DLC", "Data"])
        else:
            raise ValueError("Unsupported file format")

        df['ID'] = df['ID'].apply(lambda x: int(x, 16))  # Convert HEX to DEC
        return df
    except Exception as e:
        print(f"Error parsing log: {e}")
        return None