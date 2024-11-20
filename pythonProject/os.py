import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create an application object
app = QApplication(sys.argv)

# Create a window object
window = QWidget()
window.setWindowTitle("My First PyQt Window")
window.setGeometry(100, 100, 300, 200)

# Show the window
window.show()

# Start the application
sys.exit(app.exec_())