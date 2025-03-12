from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QCheckBox, 
    QTextEdit, QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt
from src.config.gui import (
    connection_panel, connection_panel_title,
    status_indicator_disconnected, status_indicator_connected, 
    strim_panel)

class ConnectionPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(connection_panel)
        self.setFixedSize(400, 720)  # Фиксированные размеры 
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Общие отступы панели
        layout.setSpacing(8)  # Расстояние между элементами

        # Заголовок
        self.title = QLabel("Подключение")
        self.title.setStyleSheet(connection_panel_title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setContentsMargins(0, 0, 0, 5)  # Только нижний отступ
        layout.addWidget(self.title)
        
        # Поле ввода IP
        self.ip_input = QLineEdit()
        self.apply_check = QCheckBox("Применить")
        
        # Статус подключения
        self.status_text = QLabel("Отсутствует подключение")
        self.status_indicator = QLabel()
        self.status_indicator.setFixedSize(20, 20)
        self.status_indicator.setStyleSheet(status_indicator_disconnected)
        
        # Текстовое поле вывода
        self.output_text = QTextEdit()
        self.output_text.setFixedSize(200, 100)
        self.output_text.setReadOnly(True)
        
        # Кнопки
        self.load_btn = QPushButton("Загрузить")
        self.stop_btn = QPushButton("Остановить")
        
        # Собираем интерфейс
        layout.addLayout(self._create_ip_block())
        layout.addLayout(self._create_status_block())
        layout.addWidget(self.output_text)
        layout.addLayout(self._create_button_block())
        layout.addStretch()  # Заполнит свободное пространство
        layout.addLayout(self._create_subpanels())

    def _create_ip_block(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("IP адрес:"))
        layout.addWidget(self.ip_input)
        layout.addWidget(self.apply_check)
        return layout

    def _create_status_block(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Статус подключения:"))
        layout.addWidget(self.status_text)
        layout.addWidget(self.status_indicator)
        layout.addStretch()
        return layout

    def _create_button_block(self):
        layout = QHBoxLayout()
        layout.addWidget(self.load_btn)
        layout.addWidget(self.stop_btn)
        return layout

    def _create_subpanels(self):
        layout = QHBoxLayout()
        
        left = QFrame()
        left.setLayout(QVBoxLayout())
        left.layout().addWidget(QPushButton("Загрузить"))
        
        right = QFrame()
        right.setLayout(QVBoxLayout())
        right.layout().addWidget(QPushButton("Загрузить"))
        
        layout.addWidget(left)
        layout.addWidget(right)
        return layout

    def update_status(self, connected: bool):
        self.status_indicator.setStyleSheet(
            status_indicator_connected if connected 
            else status_indicator_disconnected
        )
        self.status_text.setText(
            "Подключен" if connected 
            else "Отсутствует подключение"
        )

class StrimPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(strim_panel)
        self.setFixedSize(880, 720)  # Фиксированные размеры 
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(15)
        
        # Заголовок
        title = QLabel("Подключение")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)