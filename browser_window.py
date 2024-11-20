from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Browser")
        self.setGeometry(300, 200, 400, 300)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setStyleSheet("background-color: #000000;")

        title_bar = QWidget(self)
        title_bar.setFixedHeight(40)
        title_bar.setStyleSheet("background-color: #000000;")

        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        button_size = QSize(20, 20)
        minimize_button = QPushButton("-")
        minimize_button.setFixedSize(button_size)
        minimize_button.setStyleSheet("background-color: #444444; color: white; border: none;")
        minimize_button.clicked.connect(self.showMinimized)
        title_layout.addWidget(minimize_button)

        close_button = QPushButton("✕")
        close_button.setFixedSize(button_size)
        close_button.setStyleSheet("background-color: #ff4444; color: white; border: none;")
        close_button.clicked.connect(self.close)
        title_layout.addWidget(close_button)

        title_bar.setLayout(title_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        main_layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
