from googletrans import Translator, constants
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QLineEdit,QCheckBox
from PyQt5.QtCore import Qt 

from gtts import gTTS
import pygame
import io

translator = Translator()
# Create a subclass of QWidget for your application
class TranslateApp(QWidget):
    entered_text=''
    lang="fa"
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_field = QLineEdit()
        self.fortranslate = QLabel()
        self.change_languge = QLabel()
        self.result_label = QLabel()

        submit_button = QPushButton('translate')
        change_languge = QPushButton('change languege')
        listening_button=QPushButton('Listening')
        submit_button.clicked.connect(self.show_text)
        change_languge.clicked.connect(self.ChangeLang)
        listening_button.clicked.connect(self.speack_text)
        
        self.text_field.returnPressed.connect(submit_button.click)

        
        self.change_languge.setText(self.lang)

        layout = QVBoxLayout()
        layout.addWidget(self.change_languge)
        layout.addWidget(self.text_field)
        layout.addWidget(submit_button)
        layout.addWidget(change_languge)
        layout.addWidget(listening_button)
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
        self.entered_text = self.text_field.text()
        self.text_field.setFocus()
        
        if self.entered_text !="":
            self.fortranslate.setText(self.entered_text)
            translation = translator.translate(self.entered_text, dest="en" if self.lang=="fa" else "fa")
            self.result_label.setText(translation.text)
            
    def ChangeLang(self):
        self.lang="en" if self.lang=="fa" else "fa"
        self.change_languge.setText(self.lang)




    def speack_text(self):
        if self.entered_text !="":
            try:
                tts = gTTS(self.entered_text)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)

                # Initialize pygame mixer
                pygame.mixer.init()

                # Load and play the audio from the bytes-like object
                pygame.mixer.music.load(audio_bytes)
                pygame.mixer.music.play()

                # Wait for the audio to finish playing
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except:
                "not ok"


def main():
    app = QApplication(sys.argv)
    window = TranslateApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
