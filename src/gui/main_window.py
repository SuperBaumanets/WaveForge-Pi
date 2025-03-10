from PySide6.QtWidgets import QMainWindow, QTabWidget

from src.config.gui import window_settings, tab_settings

from .tabs.connection import ConnectionTab
from .tabs.locators import LocatorTab
from .tabs.sigFrequency import SigFreqTab
from .tabs.sigTime import SigTimeTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройка главного окна
        self.setWindowTitle(window_settings["window_title"])
        self.setGeometry(
            window_settings["initial_position"][0],
            window_settings["initial_position"][1],
            window_settings["initial_size"][0],
            window_settings["initial_size"][1]
        )
        self.setMinimumSize(
            window_settings["minimum_size"][0],
            window_settings["minimum_size"][1]
        )
        
        # Инициализация вкладок
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self._setup_tabs()
        
    def _setup_tabs(self):
        """Настройка вкладок из конфига"""
        # Применение стилей
        self.tabs.setStyleSheet(tab_settings["styles"])
        self.tabs.tabBar().setDocumentMode(tab_settings["document_mode"])
        
        # Добавление вкладок
        tab_classes = {
            "ConnectionTab": ConnectionTab,
            "LocatorTab": LocatorTab,
            "SigTimeTab": SigTimeTab,
            "SigFreqTab": SigFreqTab
        }
        
        for tab_config in tab_settings["tabs"]:
            widget_class = tab_classes[tab_config["widget"]]
            self.tabs.addTab(widget_class(), tab_config["title"])