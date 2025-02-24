from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QFileDialog, QScrollArea, QHBoxLayout, QCheckBox, QComboBox, QLineEdit

from src.gui.styles.left_panel import subtab
from src.gui.tabs.styles.subtab import main_layout, sub_layout,sub_explanations, status

class Sub3Tab1Button(QPushButton):
    def __init__(self, index, main_window, main_tab_id):
        super().__init__("SDR Устройства")
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

class Sub3Tab1Content(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self):
        self.setObjectName("container")
        layout = QVBoxLayout(self)
        self.title = QLabel("SDR устройства")

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
        launch_modes_frame = self._add_sublayouts()
        scroll_layout.addWidget(launch_modes_frame)
        scroll_layout.addStretch()
        
        # Настраиваем скролл
        scroll.setWidget(scroll_content)
        main_frame_layout.addWidget(scroll)

        # Добавляем основной контейнер в главный layout
        main.addWidget(main_frame)
        return main

    def _add_sublayouts(self):
        # Главный фрейм
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        layout = QVBoxLayout(frame)

        # Вертикально
        layout.addWidget(self._create_sdr_frame())

        return frame
    
    def _create_sdr_frame(self):
        sdr_frame = QFrame()
        sdr_frame.setStyleSheet(sub_layout)
        sdr_layout = QVBoxLayout(sdr_frame)
        sdr_layout.setContentsMargins(0, 0, 0, 0)
        sdr_layout.setSpacing(0)

        return sdr_frame