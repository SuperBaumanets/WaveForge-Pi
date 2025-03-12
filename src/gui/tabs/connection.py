from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame

from ..widgets.connection import ConnectionPanel, StrimPanel

class ConnectionTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Убираем отступы
        
        # Левая панель управления
        self.connection_panel = ConnectionPanel()
        layout.addWidget(self.connection_panel)
        
        # Правая панель (заглушка)
        right_panel = StrimPanel()
        layout.addWidget(right_panel)