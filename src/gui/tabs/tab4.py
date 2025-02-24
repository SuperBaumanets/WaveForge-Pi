from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ._tab4.subtab1 import Sub1Tab4Button

from src.gui.styles.left_panel import tab

class Tab4(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.main_tab_id = 4
        self.subtabs = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.main_button = QPushButton("Сигналы в частотной области")
        self.main_button.setStyleSheet(tab)
        self.main_button.setCheckable(True)
        self.main_button.clicked.connect(self.toggle_subtabs)

        self.subtab1 = Sub1Tab4Button(6, self.main_window, self.main_tab_id)
        
        layout.addWidget(self.main_button)
        layout.addWidget(self.subtab1)
    
        self.subtab1.hide()   

    def toggle_subtabs(self):
        expanded = self.main_button.isChecked()
        self.subtab1.setVisible(expanded)

        # Восстанавливаем активный подтаб, если он принадлежит этому табу
        if expanded:
            last_subtab = self.main_window.last_active_subtab
            if last_subtab and last_subtab.main_tab_id == self.main_tab_id:
                last_subtab.setChecked(True)