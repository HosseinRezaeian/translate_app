from googletrans import Translator, constants
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QLineEdit,QCheckBox
from PyQt5.QtCore import Qt 
translator = Translator()
# Create a subclass of QWidget for your application
class TranslateApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_field = QLineEdit()
        self.fortranslate = QLabel()

        self.result_label = QLabel()

        submit_button = QPushButton('translate')
        submit_button.clicked.connect(self.show_text)
        self.text_field.returnPressed.connect(submit_button.click)




        layout = QVBoxLayout()
        layout.addWidget(self.text_field)
        layout.addWidget(submit_button)
        layout.addWidget(self.fortranslate)
        layout.addWidget(self.result_label)




        self.checkbox = QCheckBox('Make Window Topmost')
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.checkbox.stateChanged.connect(self.toggle_topmost)

       
        self.setLayout(layout)

        self.setWindowTitle('Translate app')
        self.setGeometry(100, 100, 400, 200)
        # layout.addWidget(self.checkbox) 





    def toggle_topmost(self, state):
        if state == Qt.Checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            print('yes')
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnBottomHint)
            print('no')

        self.show()
        
    def show_text(self):
        entered_text = self.text_field.text()
        self.text_field.clear()
        if entered_text !="":
            self.fortranslate.setText(entered_text)
            translation = translator.translate(entered_text, dest="fa")
            self.result_label.setText(translation.text)


def main():
    app = QApplication(sys.argv)
    window = TranslateApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
