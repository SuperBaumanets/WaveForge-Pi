from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SigFreqTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Сигнал во частотной области"))