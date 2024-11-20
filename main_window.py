from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from browser_window import BrowserWindow
from custom_window import CustomWindow
from icon_label import IconLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setWindowTitle("PyQt5 Full Black Theme")
        self.setGeometry(100, 100, 1200, 600)
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

        maximize_button = QPushButton("⬜")
        maximize_button.setFixedSize(button_size)
        maximize_button.setStyleSheet("background-color: #444444; color: white; border: none;")
        maximize_button.clicked.connect(self.toggleMaxRestore)
        title_layout.addWidget(maximize_button)

        close_button = QPushButton("✕")
        close_button.setFixedSize(button_size)
        close_button.setStyleSheet("background-color: #ff4444; color: white; border: none;")
        close_button.clicked.connect(self.close)
        title_layout.addWidget(close_button)

        title_bar.setLayout(title_layout)

        background_label = QLabel(self)
        background_pixmap = QPixmap("background.png")
        background_pixmap = background_pixmap.scaled(1200, 800, Qt.KeepAspectRatioByExpanding)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 40, 1200, 800)

        sidebar_width = 80
        sidebar = QWidget(self)
        sidebar.setGeometry(0, 40, sidebar_width, 760)
        sidebar.setStyleSheet("background-color: #222222;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        icons = ["1.png", "3.png", "4.png", "2.png"]
        for i, icon_path in enumerate(icons):
            icon_label = IconLabel(icon_path)
            layout.addWidget(icon_label)
            if i == 0:
                icon_label.mousePressEvent = self.openBrowserWindow
            elif i == 2:
                icon_label.mousePressEvent = self.openCustomWindow

        sidebar.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)
        main_layout.addWidget(background_label)

        self.show()

    def openBrowserWindow(self, event):
        self.browser_window = BrowserWindow()
        self.browser_window.show()

    def openCustomWindow(self, event):
        self.custom_window = CustomWindow()
        self.custom_window.show()

    def toggleMaxRestore(self):
        if self.isMaximized:
            self.showNormal()
        else:
            self.showMaximized()
        self.isMaximized = not self.isMaximized

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
