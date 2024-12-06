from PyQt6 import uic
import os

from PyQt6.uic.uiparser import QtWidgets

from ..parser.log_parser import parse_log
from ..parser.dbc_parser import load_dbc
from reporter.report_generator import generate_report
from validator.data_validator import validate_data


class MainGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/main_window.ui"), self)

        # Connect buttons to functions
        self.loadLogButton.clicked.connect(self.load_log_file)
        self.loadDBCButton.clicked.connect(self.load_dbc_file)
        self.validateButton.clicked.connect(self.validate_data)
        self.generateReportButton.clicked.connect(self.generate_report)

        # File paths
        self.log_file_path = ""
        self.dbc_file_path = ""
        self.errors = []

    def load_log_file(self):
        self.log_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Log File", "logs", "Log Files (*.csv *.txt)")
        if self.log_file_path:
            self.logFilePathDisplay.setText(self.log_file_path)

    def load_dbc_file(self):
        self.dbc_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open DBC File", "dbc", "DBC Files (*.dbc)")
        if self.dbc_file_path:
            self.dbcFilePathDisplay.setText(self.dbc_file_path)

    def validate_data(self):
        if not self.log_file_path or not self.dbc_file_path:
            QtWidgets.QMessageBox.warning(self, "Error", "Please load both log and DBC files.")
            return

        log_data = parse_log(self.log_file_path)
        dbc = load_dbc(self.dbc_file_path)
        if log_data is not None and dbc is not None:
            self.errors = validate_data(log_data, dbc)
            self.validationResultsDisplay.setText(f"Validation completed: {len(self.errors)} errors found.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to load log or DBC file.")

    def generate_report(self):
        if not self.errors:
            QtWidgets.QMessageBox.warning(self, "Error", "No errors to generate report.")
            return

        save_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Report", "output/validation_report.xlsx", "Excel Files (*.xlsx)")
        if save_path:
            generate_report(self.errors, save_path)
            QtWidgets.QMessageBox.information(self, "Success", f"Report saved to {save_path}.")