from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class IconLabel(QLabel):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(icon_path).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
    def mousePressEvent(self, event):
        if self.parent():
            self.parent().iconClicked(self)
