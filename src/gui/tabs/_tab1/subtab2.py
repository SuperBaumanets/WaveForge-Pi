from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QTextEdit, QScrollArea, QHBoxLayout, QLineEdit

from datetime import datetime

from src.gui.styles.left_panel import subtab
from src.gui.tabs.styles.subtab import main_layout, sub_layout,sub_explanations, status
from src.core.tabs.subtab2 import SubTab2ActionHandler

class Sub2Tab1Button(QPushButton):
    def __init__(self, index, main_window, main_tab_id):
        super().__init__("Запуск на Raspberry Pi")
        self.index = index
        self.main_window = main_window
        self.main_tab_id = main_tab_id
        self.setCheckable(True) 
        self.setStyleSheet(subtab)
        self.setContentsMargins(0, 0, 0, 0)
        self.clicked.connect(self.show_content)
    
    def show_content(self):
        self.main_window.set_active_subtab(self)
        self.main_window.show_content(self.index)

class Sub2Tab1Content(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self):
        self.setObjectName("container")
        layout = QVBoxLayout(self)
        self.title = QLabel("Запуск на Raspberry Pi")

        # Собираем интерфейс
        layout.addWidget(self.title)
        layout.addLayout(self._create_sublayouts())
        layout.addStretch()

    def _create_sublayouts(self):
        # Главный layout, который будет возвращен
        main = QVBoxLayout()

        # Создаем основной контейнер
        main_frame = QFrame()
        main_frame.setStyleSheet(main_layout) 
        main_frame_layout = QVBoxLayout(main_frame)
        main_frame_layout.setContentsMargins(0, 0, 0, 0)
        # Создаем скролл-область
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumSize(600, 550)
        scroll.setMaximumWidth(1000)
        
        # Контейнер для прокручиваемого контента
        scroll_content = QWidget()
        scroll_content.setStyleSheet(main_layout)
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        
        # Добавляем дочерние элементы в скролл
        launch_modes_frame = self._create_launch_modes_frame()
        scroll_layout.addWidget(launch_modes_frame)
        scroll_layout.addStretch()
        
        # Настраиваем скролл
        scroll.setWidget(scroll_content)
        main_frame_layout.addWidget(scroll)

        # Добавляем основной контейнер в главный layout
        main.addWidget(main_frame)
        return main

    def _create_connection_frame(self):
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        layout = QVBoxLayout(frame)

        label_title = QLabel("Подключение")
        label_title.setStyleSheet(sub_layout)
        layout.addWidget(label_title)

        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        status_frame = QFrame()
        status_frame.setStyleSheet(status)
        status_layout = QVBoxLayout(status_frame)
        status_layout.setSpacing(0)

        status_label = QLabel("Статус")
        status_label.setStyleSheet(sub_layout)
        status_layout.addWidget(status_label)

        device_status_frame = QFrame()
        device_status_frame.setStyleSheet(sub_layout)
        device_layout = QHBoxLayout(device_status_frame)

        self.status_indicator = QLabel("DISCONNECTED")
        self.status_indicator.setStyleSheet("color: #C40000; font-size: 16px;")
        device_name = QLabel("Raspberry PI:")

        device_layout.addWidget(device_name)
        device_layout.addWidget(self.status_indicator)
        device_layout.addStretch()

        status_layout.addWidget(device_status_frame)
        status_layout.addStretch()


        form_frame = QFrame()
        form_frame.setStyleSheet(sub_layout)
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(15)

        ip_layout = QHBoxLayout()
        ip_label = QLabel("IP адрес:")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("192.168.1.100")
        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(self.ip_input)

        pass_layout = QHBoxLayout()
        pass_label = QLabel("Пароль: ")
        self.pass_input = QLineEdit()
        #self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setPlaceholderText("Введите пароль")
        pass_layout.addWidget(pass_label)
        pass_layout.addWidget(self.pass_input)

        self.connect_btn = QPushButton("Подключиться")
        self.connect_btn.clicked.connect(self._handle_connection)
        self.connect_btn.setStyleSheet(sub_layout)

        form_layout.addLayout(ip_layout)
        form_layout.addLayout(pass_layout)
        form_layout.addWidget(self.connect_btn)
        form_layout.addStretch()

        content_layout.addWidget(form_frame)
        content_layout.addWidget(status_frame)
        layout.addWidget(content_widget)

        return frame

    def _create_launch_modes_frame(self):
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        layout = QVBoxLayout(frame)

        layout.addWidget(self._create_connection_frame())

        label_title = QLabel("Режимы запуска модели")
        label_title.setStyleSheet(sub_layout)
        layout.addWidget(label_title)

        static_block = self._create_loading(
            "Режим статической загрузки",
            "Код загружается в устройство как фиксированная прошивка, где все параметры жестко заданы\n на этапе компиляции.",
            "Запустить излучение", 
            SubTab2ActionHandler.run_static_emitting
        )
        layout.addWidget(static_block)

        dynamic_block = self._create_loading(
            "Режим динамической загрузки", 
            "Код загружается с поддержкой протокола XCP (Universal Measurement and Calibration Protocol),\n что позволяет изменять параметры излучаемого сигнала в реальном времени.",
            "Запустить излучение",
            SubTab2ActionHandler.run_dynamic_emitting
        )
        layout.addWidget(dynamic_block)

        stop_button = QPushButton("Остановить излучение")
        stop_button.clicked.connect(SubTab2ActionHandler.stop_emitting)
        stop_button.setFixedSize(200, 30)
        layout.addWidget(stop_button)

        layout.addWidget(self._create_info())

        return frame
    
    def _create_loading(self, title:str, explanations:str, button:str, function:object):
        loading_container = QFrame()
        loading_container.setStyleSheet(sub_layout)
        loading_layout = QVBoxLayout(loading_container)
        loading_layout.setSpacing(0)

        loading_title = QLabel(title)
        loading_explanations = QLabel(explanations)
        loading_explanations.setStyleSheet(sub_explanations)
        loading_button = QPushButton(button)
        loading_button.setFixedSize(200, 30)
        loading_button.clicked.connect(function)

        loading_layout.addWidget(loading_title)
        loading_layout.addWidget(loading_explanations)
        loading_layout.addWidget(loading_button)

        return loading_container

    def _create_info(self):
        info_container = QFrame()
        info_container.setStyleSheet(sub_layout)
        info_layout = QVBoxLayout(info_container)
        info_layout.setSpacing(0)

        self.log_output = QTextEdit()
        self.log_output.setMinimumSize(600, 200)
        self.log_output.ensureCursorVisible()
        self.log_output.setReadOnly(True)

        # Подключение сигнала обновления лога
        SubTab2ActionHandler.connect_log_signal(self.append_to_log)

        log_text = QLabel("Информация о процессах:")
        log_text.setStyleSheet(sub_layout)

        info_layout.addWidget(log_text)
        info_layout.addWidget(self.log_output)

        return info_container

    def append_to_log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_output.append(f"[{timestamp}] {message}")

        cursor = self.log_output.textCursor()
        self.log_output.setTextCursor(cursor)

    def _handle_connection(self):
        connected = SubTab2ActionHandler.connect_to_target()

        if connected:
            self.status_indicator.setText("CONNECTED")
            self.status_indicator.setStyleSheet("color: #00C023; font-size: 16px;")
        else:
            self.status_indicator.setText("DISCONNECTED")
            self.status_indicator.setStyleSheet("color: #C40000; font-size: 16px;")