import cantools

def load_dbc(file_path):
    try:
        db = cantools.database.load_file(file_path)
        return db
    except Exception as e:
        print(f"Error loading DBC file: {e}")
        return None