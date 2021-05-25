import sys
import syntax_pars
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TextEditor(QtWidgets.QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self.resize(1280, 800)

    def keyPressEvent(self, event):
        character_list = {
            '[': ']',
            '(': ')',
            "'": "'",
            '"': '"',
            '{': '}'
        }

        closing_char = character_list.get(event.text())

        if closing_char:
            char_cusor = self.textCursor()
            char_position1 = char_cusor.position()

            self.insertPlainText(closing_char)
            char_cusor.setPosition(char_position1)
            self.setTextCursor(char_cusor)
        super().keyPressEvent(event)


app = QApplication(sys.argv)
textEditor = TextEditor()
textEditor.setStyleSheet("""QPlainTextEdit{
	font-family:'Consolas';
	color: #ccc; 
	background-color: #2b2b2b;}""")
textEditor.setWindowTitle("Pyter")
highlight = syntax_pars.PythonHighlighter(textEditor.document())
textEditor.setFont(QFont('Open Sans', 13))
textEditor.setWindowIcon(QtGui.QIcon('pyter.png'))
textEditor.showMaximized()

sys.exit(app.exec_())
