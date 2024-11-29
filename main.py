import sys

from PyQt5 import QtWidgets
from gui.main_gui import MainGUI

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = MainGUI()
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

