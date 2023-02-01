import sys
from find_word import find_all_files_in_dir
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QScrollArea, QWidget, QLabel, QPlainTextEdit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dinara help")
        self.resize(1200, 600)

        self.text_input = QPlainTextEdit("Введи слово, которое нужно найти\n"
                                        "Нажми кнопку \"Select directory\"\n"
                                        "Нажми кнопку \"Start\"\n"
                                        "Внизу будет список всех файлов в этой директории (и поддиректориях), в которых нашлось нужное слово")
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.button = QPushButton("Start")
        self.button.setEnabled(False)
        self.directory_button = QPushButton("Select Directory")
        self.close_button = QPushButton("Close")

        self.button.clicked.connect(self.change_text)
        self.close_button.clicked.connect(app.quit)
        self.directory_button.clicked.connect(self.select_directory)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.directory_button)
        button_layout.addWidget(self.close_button)
        button_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.text_input)
        main_layout.addWidget(self.scroll_area)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def select_directory(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.scroll_area.setWidget(QPlainTextEdit(""))
        if self.directory != "":
            self.button.setEnabled(True)

    def change_text(self):
        self.substring = self.text_input.toPlainText()
        files = find_all_files_in_dir(self.directory, self.substring)
        text = ""
        for file in files:
            text += file + "\n"
        self.scroll_area.setWidget(QPlainTextEdit(text))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
