from PyQt5 import QtWidgets
from exel_utility_ui import Ui_Form
from format_spreadsheet import format_spreadsheet
import sys


class ExelUtilityApp(QtWidgets.QWidget):
    def __init__(self):
        super(ExelUtilityApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.do_it_button.clicked.connect(self.do_it_btn_clicked)

    def do_it_btn_clicked(self):
        file_path = self.ui.file_path_lineEdit.text()
        new_file_name = self.ui.new_file_name_lineEdit.text()
        print(file_path)
        print(new_file_name)
        print('aaaaaaa')
        format_spreadsheet(file_path, new_file_name)


app = QtWidgets.QApplication([])
application = ExelUtilityApp()
application.show()
sys.exit(app.exec())
