from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QCheckBox, 
    QTextEdit, QPushButton
)

import datetime

from PySide6.QtCore import Qt

import pyqtgraph as pg
import numpy as np

from src.config.widgets.connection import (
    connection_panel, connection_panel_title, 
    connection_panel_subpanels, connection_panel_subpanels_text, connection_panel_subpanels_title,
    status_indicator_disconnected, status_indicator_connected)

class ConnectionPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(connection_panel)
        self.setFixedSize(420, 720)  # Фиксированные размеры 
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
        self.ip_addr_text = QLabel("IP адрес:")
        self.ip_input = QLineEdit()
        self.ip_input.setFocus()
        self.apply_btn = QPushButton("Применить")
        
        # Статус подключения
        self.status_ip_text = QLabel("Статус подключения:")
        self.status_text = QLabel("Отсутствует подключение")
        self.status_indicator = QLabel()
        self.status_indicator.setFixedSize(20, 20)
        self.status_indicator.setStyleSheet(status_indicator_disconnected)
        
        # Текстовое поле вывода
        self.log_output = QTextEdit()
        self.log_output.setFixedSize(400, 200)
        self.log_output.ensureCursorVisible()
        self.log_output.setReadOnly(True)
        self.log_text = QLabel("Информация о процессах:")
        
        # Кнопки
        self.stop_btn = QPushButton("Остановить излучение")

        # Заголовок режима запуска
        self.launch_mode = QLabel("Режим запуска:")
        
        # Собираем интерфейс
        layout.addLayout(self._create_ip_block())
        layout.addLayout(self._create_status_block())
        layout.addWidget(self.launch_mode)
        layout.addLayout(self._create_subpanels())
        layout.addLayout(self._create_button_block())
        layout.addStretch()

    def _create_ip_block(self):
        layout = QHBoxLayout()
        layout.addWidget(self.ip_addr_text)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.apply_btn)
        return layout

    def _create_status_block(self):
        main_layout = QVBoxLayout()

        status_layout = QHBoxLayout()
        status_layout.addWidget(self.status_ip_text)
        status_layout.addWidget(self.status_text)
        status_layout.addWidget(self.status_indicator)
        status_layout.addStretch()

        main_layout.addLayout(status_layout)
        main_layout.addWidget(self.log_text)
        main_layout.addWidget(self.log_output)

        return main_layout

    def _create_button_block(self):
        layout = QHBoxLayout()
        layout.addWidget(self.stop_btn)
        return layout

    def _create_subpanels(self):
        layout = QHBoxLayout()
        
        left = QFrame()
        left.setStyleSheet(connection_panel_subpanels)
        left.setFixedSize(195, 215)
        left.setLayout(QVBoxLayout())
        label_ltitle = QLabel("Deployment Mode")
        label_ltitle.setStyleSheet(connection_panel_subpanels_title)
        left.layout().addWidget(label_ltitle)
        
        left.layout().addWidget(QPushButton("Запустить"))

        label = QLabel("Запуск приложения\n на raspberry pi.\n Обратная связь\n недоступна.\n")
        label.setStyleSheet(connection_panel_subpanels_text)
        left.layout().addWidget(label)
        
        right = QFrame()
        right.setStyleSheet(connection_panel_subpanels)
        right.setFixedSize(195, 215)
        right.setLayout(QVBoxLayout())
        label_rtitle = QLabel("Live Control Mode")
        label_rtitle.setStyleSheet(connection_panel_subpanels_title)
        right.layout().addWidget(label_rtitle)

        right.layout().addWidget(QPushButton("Запустить"))
        
        label = QLabel("Запуск приложения\nна raspberry pi.\nИзменение параметров\nсигнала во время\nизлучения.")
        label.setStyleSheet(connection_panel_subpanels_text)
        right.layout().addWidget(label)
        
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

    def update_log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_output.append(f"[{timestamp}] {message}")

class StrimPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(connection_panel)
        self.setFixedSize(860, 720)  # Фиксированные размеры 
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Общие отступы панели
        layout.setSpacing(8)  # Расстояние между элементами

        # Заголовок
        self.title = QLabel("Стримминг данных")
        self.title.setStyleSheet(connection_panel_title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setContentsMargins(0, 0, 0, 5)  # Только нижний отступ
        layout.addWidget(self.title)

        # Заголовок графика
        self.graph_text = QLabel("Данные подаваемые на излучатель:")

        # Собираем интерфейс
        layout.addWidget(self.graph_text)
        layout.addLayout(self._create_graph())
        layout.addStretch()
    
    def _create_graph(self):
        # Создаем графический виджет
        self.graph_widget = pg.PlotWidget()
        
        # Настройка стиля графика
        self.graph_widget.setBackground('#FFFFFF')
        self.graph_widget.showGrid(x=True, y=True, alpha=0.9)
        self.graph_widget.setLabel('left', 'Амплитуда')
        self.graph_widget.setLabel('bottom', 'Время, с')
        
        # Инициализируем пустой график
        self.plot_data = self.graph_widget.plot(pen=pg.mkPen('#000000', width=2))

        layout = QVBoxLayout()
        layout.addWidget(self.graph_widget)
        return layout

    def update_graph_data(self, x_data, y_data):
        """Обновление данных графика"""
        # Конвертируем в numpy массивы для оптимизации
        x = np.array(x_data)
        y = np.array(y_data)
        
        # Обновляем данные
        self.plot_data.setData(x, y)
        
        # Автомасштабирование
        self.graph_widget.autoRange()