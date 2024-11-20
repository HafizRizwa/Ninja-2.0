from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Window")
        self.setGeometry(400, 250, 600, 400)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setStyleSheet("background-color: #2c2c2c; color: white;")

        title_bar = QWidget(self)
        title_bar.setFixedHeight(40)
        title_bar.setStyleSheet("background-color: #000000;")

        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        minimize_button = QPushButton("-")
        minimize_button.setFixedSize(20, 20)
        minimize_button.setStyleSheet("background-color: #444444; color: white; border: none;")
        minimize_button.clicked.connect(self.showMinimized)
        title_layout.addWidget(minimize_button)

        close_button = QPushButton("✕")
        close_button.setFixedSize(20, 20)
        close_button.setStyleSheet("background-color: #ff4444; color: white; border: none;")
        close_button.clicked.connect(self.close)
        title_layout.addWidget(close_button)

        title_bar.setLayout(title_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
