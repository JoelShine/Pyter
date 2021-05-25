# Pyter
The Ultimate Text Editor, with complete features including syntax highlighting and bracket autocomplete, made purely from Python.

Currently, only supports writing, other features will be included shortly.

Code Structure
--------------
The **"syntax_pars.py"** contains the code for syntax higlighting. The autocomplete feature for brackets and single and double quotation marks is in the below peice of code :
```python
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
```
Above is a function in the **"Pyter.py"** file.
