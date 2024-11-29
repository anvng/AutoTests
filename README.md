# Automotive Data/Log Tool

## Overview

This project is a GUI application that provides functionalities for loading log and DBC files, validating the data, and generating reports based on validation results. It utilizes PyQt5 for the graphical user interface and processes data using pandas and cantools.

## Features

- Load log files in CSV or TXT format.
- Load DBC files for CAN message definitions.
- Validate log data against DBC specifications.
- Generate Excel reports of validation errors.

## Requirements

- Python 3.11
- PyQt5
- pandas
- cantools
- openpyxl

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:anvng/AutomotiveLogTool.git
   ```
2. Navigate to the project directory:
   ```
   cd AutomotiveLogTool
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python main.py
   ```
2. Use the GUI to load log and DBC files.
3. Validate the loaded data.
4. Generate a report of the validation results.

## Project Structure

- `gui/`: Contains the main GUI application files.
- `parser/`: Includes modules for parsing log and DBC files.
- `validator/`: Contains the data validation logic.
- `reporter/`: Handles report generation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.