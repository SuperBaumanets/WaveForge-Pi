from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QFileDialog, QScrollArea, QHBoxLayout, QCheckBox, QComboBox, QLineEdit

import os

from src.gui.styles.left_panel import subtab
from src.gui.tabs.styles.subtab import main_layout, sub_layout,sub_explanations, status
from src.core.tabs.subtab2 import SubTab2ActionHandler

class Sub1Tab2Button(QPushButton):
    def __init__(self, index, main_window, main_tab_id):
        super().__init__("Управление локаторами")
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

class Sub1Tab2Content(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self):
        self.setObjectName("container")
        layout = QVBoxLayout(self)
        self.title = QLabel("Управление локаторами")

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
        layout.addWidget(self._create_avaible_locators_frame())
        layout.addWidget(self._create_download_locators_frame())

        # Контейнер для Горизонтальных
        h_frame = QFrame()
        h_frame.setStyleSheet(status)
        h_layout = QHBoxLayout(h_frame)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(0)

        # Горизонтально
        h_layout.addWidget(self._create_locators_characteristics_frame())
        h_layout.addWidget(self._create_locators_control_frame())

        layout.addWidget(h_frame)

        return frame
    
    def _create_avaible_locators_frame(self):
        # Основной контейнер
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        main_layout = QVBoxLayout(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        title_label = QLabel("Список доступных локаторов")
        title_label.setStyleSheet(sub_layout)
        main_layout.addWidget(title_label)

        selector_frame = QFrame()
        selector_frame.setStyleSheet(status)
        selector_layout = QHBoxLayout(selector_frame)
        selector_layout.setContentsMargins(0, 0, 0, 0)
        selector_layout.setSpacing(0)

        combo_label = QLabel("Выбрать локатор из списка:")
        combo_label.setStyleSheet(sub_explanations)

        self.locator_combo = QComboBox()
        self.locator_combo.setStyleSheet(sub_layout)
        self.locator_combo.addItems([" Выберите элемент", "Локатор 1", "Локатор 2", "Локатор 3"])
        self.locator_combo.setFixedWidth(500)

        selector_layout.addWidget(combo_label)
        selector_layout.addWidget(self.locator_combo)
        selector_layout.addStretch()

        main_layout.addWidget(selector_frame)
        main_layout.addStretch()

        return frame
    
    def _create_download_locators_frame(self):
        # Основной контейнер
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        main_layout = QVBoxLayout(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Заголовок контейнера
        title_frame = QLabel("Использование имеющихся конфигураций локаторов")
        title_frame.setStyleSheet(sub_layout)
        main_layout.addWidget(title_frame)

        # Загрузка конфигурации локатора:
        dwnl_cnfg_frame = QFrame()
        dwnl_cnfg_frame.setStyleSheet(status)
        dwnl_cnfg_layout = QHBoxLayout(dwnl_cnfg_frame)
        dwnl_cnfg_layout.setContentsMargins(0, 0, 0, 0)
        dwnl_cnfg_layout.setSpacing(0)

        dwnl_cnfg_label = QLabel("Загрузка конфигурации локатора:")
        dwnl_cnfg_label.setStyleSheet(sub_explanations)

        slct_lctr_button = QPushButton("Выбрать TOML-файл:")
        slct_lctr_button.setStyleSheet(sub_layout)
        slct_lctr_button.clicked.connect(self._open_file_dialog)
        slct_lctr_button.setFixedWidth(300)

        # Выбор локатора из списка:
        slct_lctr_frame = QFrame()
        slct_lctr_frame.setStyleSheet(status)
        slct_lctr_layout = QHBoxLayout(slct_lctr_frame)
        slct_lctr_layout.setContentsMargins(0, 0, 0, 0)
        slct_lctr_layout.setSpacing(0)

        slct_lctr_label = QLabel("Выбрать локатор из списка:              ")
        slct_lctr_label.setStyleSheet(sub_explanations)

        slct_lctr_combo = QComboBox()
        slct_lctr_combo.setStyleSheet(sub_layout)
        slct_lctr_combo.addItems([" Выберите элемент", "Локатор 1", "Локатор 2", "Локатор 3"])
        slct_lctr_combo.setFixedWidth(450)

        # Автоматический расчет характеристик локатора
        auto_calc_chrtcs_frame = QFrame()
        auto_calc_chrtcs_frame.setStyleSheet(status)
        auto_calc_chrtcs_layout = QHBoxLayout(auto_calc_chrtcs_frame)
        auto_calc_chrtcs_layout.setContentsMargins(0, 0, 0, 0)
        auto_calc_chrtcs_layout.setSpacing(0)

        auto_calc_chrtcs_label = QLabel("Рассчитывать недостающие\n характеристики локатора:                  ")
        auto_calc_chrtcs_label.setStyleSheet(sub_explanations)

        auto_calc_chrtcs_сheckbox = QCheckBox("")
        auto_calc_chrtcs_сheckbox.stateChanged.connect(self._on_checkbox_changed)

        dwnl_cnfg_layout.addWidget(dwnl_cnfg_label)
        dwnl_cnfg_layout.addWidget(slct_lctr_button)
        dwnl_cnfg_layout.addStretch()
        slct_lctr_layout.addWidget(slct_lctr_label)
        slct_lctr_layout.addWidget(slct_lctr_combo)
        slct_lctr_layout.addStretch()
        auto_calc_chrtcs_layout.addWidget(auto_calc_chrtcs_label)
        auto_calc_chrtcs_layout.addWidget(auto_calc_chrtcs_сheckbox)
        auto_calc_chrtcs_layout.addStretch()

        main_layout.addWidget(dwnl_cnfg_frame)
        main_layout.addWidget(slct_lctr_frame)
        main_layout.addWidget(auto_calc_chrtcs_frame)
        main_layout.addStretch()

        return frame
    
    def _create_locators_characteristics_frame(self):
        lctr_chrtcs_frame = QFrame()
        lctr_chrtcs_frame.setStyleSheet(sub_layout)
        lctr_chrtcs_layout = QVBoxLayout(lctr_chrtcs_frame)
        lctr_chrtcs_layout.setContentsMargins(0, 0, 0, 0)
        lctr_chrtcs_layout.setSpacing(0)

        # Заголовок контейнера
        title_frame = QLabel("Характеристики выбранного локатора")
        title_frame.setStyleSheet(sub_layout)
        lctr_chrtcs_layout.addWidget(title_frame)

        parameter_names = [
            "Название локатора:",
            "Тип сигнала:",
            "Рабочий диапазон частот, Гц:",
            "Период повторения импульсов, мкс:",
            "Частота повторения импульсов, Гц:",
            "Длительность импульса, мкс:",
            "Количество импульсов, шт:"
        ]

        # Создаем группы элементов
        for name in parameter_names:
            group_frame = QFrame()
            group_frame.setStyleSheet(status)
            group_layout = QHBoxLayout(group_frame)
            group_layout.setContentsMargins(0, 0, 0, 0)

            label = QLabel(name)
            label.setStyleSheet(sub_explanations)
            edit = QLineEdit()
            edit.setStyleSheet(sub_layout)
            edit.setFixedSize(200, 30)

            group_layout.addWidget(label)
            group_layout.addWidget(edit)
            lctr_chrtcs_layout.addWidget(group_frame)

        lctr_chrtcs_layout.addStretch()

        return lctr_chrtcs_frame
    
    def _create_locators_control_frame(self):
        lctr_cntrl_frame = QFrame()
        lctr_cntrl_frame.setStyleSheet(sub_layout)
        lctr_cntrl_layout = QVBoxLayout(lctr_cntrl_frame)
        lctr_cntrl_layout.setContentsMargins(0, 0, 0, 0)
        lctr_cntrl_layout.setSpacing(0)

        # Заголовок контейнера
        title_frame = QLabel("Управление")
        title_frame.setStyleSheet(sub_layout)

        # Добавление локатора
        add_lctr_label = QLabel("Добавить текущий локатора в\n общий список локаторов:")
        add_lctr_label.setStyleSheet(sub_explanations)

        add_button = QPushButton("Добавить")
        add_button.setFixedSize(200, 30)

        # Удаление локатора
        del_lctr_label = QLabel("Удалить текущий локатор из\n общего списка локаторов:")
        del_lctr_label.setStyleSheet(sub_explanations)

        del_button = QPushButton("Удалить")
        del_button.setFixedSize(200, 30)

        lctr_cntrl_layout.addWidget(title_frame)
        lctr_cntrl_layout.addWidget(add_lctr_label)
        lctr_cntrl_layout.addWidget(add_button)
        lctr_cntrl_layout.addWidget(del_lctr_label)
        lctr_cntrl_layout.addWidget(del_button)
        lctr_cntrl_layout.addStretch()

        return lctr_cntrl_frame
    
    def _on_checkbox_changed(self, state):
        if state == 2:
            print("Чекбокс активирован")
        else:
            print("Чекбокс деактивирован")

    def _open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите TOML-файл",
            os.path.expanduser("~"), 
            "TOML Files (*.toml)",
            options=options
        )
        
        if file_path:
            self.selected_file = os.path.normpath(file_path)
            print(f"Выбран файл: {self.selected_file}")