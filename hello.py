from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import psutil
import sys

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser")
        self.setGeometry(300, 200, 600, 400)
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

class ProcessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Monitor")
        self.setGeometry(450, 250, 400, 300)
        self.setStyleSheet("background-color: #1a1a1a; color: white;")
        
        layout = QVBoxLayout()
        
        # Round "Click" button to start the process
        self.start_button = QPushButton("Click")
        self.start_button.setFixedSize(100, 100)
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #00ccff;
                border-radius: 50px;
                font-size: 18px;
                color: white;
            }
            QPushButton:hover {
                background-color: #0099cc;
            }
        """)
        self.start_button.clicked.connect(self.startProcess)
        
        # Memory statistics label
        self.memory_label = QLabel("Memory Usage: 0%")
        self.memory_label.setFont(QFont("Arial", 16))
        self.memory_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.memory_label, alignment=Qt.AlignCenter)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Timer to update memory usage
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateMemoryUsage)

    def startProcess(self):
        # Start memory statistics display
        if not self.timer.isActive():
            self.timer.start(1000)  # Update every second

    def updateMemoryUsage(self):
        memory = psutil.virtual_memory()
        self.memory_label.setText(f"Memory Usage: {memory.percent}%")

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
        
        self.isMaximized = False
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
        background_pixmap = QPixmap("background.png").scaled(1200, 800, Qt.KeepAspectRatioByExpanding)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 40, 1200, 800)
        
        sidebar_width = 80
        icon_size = QSize(40, 40)

        sidebar = QWidget(self)
        sidebar.setGeometry(0, 40, sidebar_width, 760)
        sidebar.setStyleSheet("background-color: #222222;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        icons = ["1.png", "3.png", "4.png", "2.png"]
        for i, icon_path in enumerate(icons):
            icon_label = QLabel()
            icon_pixmap = QPixmap(icon_path).scaled(icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(icon_pixmap)
            layout.addWidget(icon_label)
            
            if i == 0:
                icon_label.mousePressEvent = self.openBrowserWindow
            elif i == 2:
                icon_label.mousePressEvent = self.openProcessWindow
            elif i == 3:
                icon_label.mousePressEvent = self.openCustomWindow

        sidebar.setLayout(layout)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)
        main_layout.addWidget(background_label)

        self.show()

    def openBrowserWindow(self, event):
        self.browser_window = BrowserWindow()
        self.browser_window.show()

    def openProcessWindow(self, event):
        self.process_window = ProcessWindow()
        self.process_window.show()
    
    def openCustomWindow(self, event):
        self.custom_window = CustomWindow()
        self.custom_window.show()

    def toggleMaxRestore(self):
        if self.isMaximized:
            self.showNormal()
        else:
            self.showMaximized()
        self.isMaximized = not self.isMaximized

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
sys.exit(app.exec_())