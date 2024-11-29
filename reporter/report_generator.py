import pandas as pd

def generate_report(errors, output_path):
    try:
        df = pd.DataFrame(errors)
        df.to_excel(output_path, index=False)
    except Exception as e:
        print(f"Error generating report: {e}")