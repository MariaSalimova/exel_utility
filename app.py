from PyQt5 import QtWidgets
from exel_utility_ui import Ui_Form
import sys


class ExelUtilityApp(QtWidgets.QWidget):
    def __init__(self):
        super(ExelUtilityApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = ExelUtilityApp()
application.show()
sys.exit(app.exec())
