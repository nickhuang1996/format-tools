from scripts.Form.SelectForm import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    selectform = SelectForm("format tools")
    selectform.show()
    sys.exit(app.exec_())
