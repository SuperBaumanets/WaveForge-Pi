from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QFileDialog, QScrollArea, QHBoxLayout, QCheckBox, QComboBox, QLineEdit

import os

from src.gui.styles.left_panel import subtab
from src.gui.tabs.styles.subtab import main_layout, sub_layout,sub_explanations, status
from src.core.actions.locatormanager_action import LocatorManagerActionHandler

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
        self.lctrs_avaible = None
        self.lctr_avaible_handler = LocatorManagerActionHandler("src/resources/data/locators.toml")
        self.lctr_download_handler = None
        super().__init__()
        self._setup_ui()
        self._connect_settings()
    
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
        self.lctrs_avaible = self.lctr_avaible_handler.get_locators()
        self.ordered_lctrs = ["Выберите элемент"]
        for locator in self.lctrs_avaible:
            if locator != "Выберите элемент" and locator not in self.ordered_lctrs:
                self.ordered_lctrs.append(locator)
        
        # Основной контейнер
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        main_layout = QVBoxLayout(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Заголовок контейнера
        title_label = QLabel("Список доступных локаторов")
        title_label.setStyleSheet(sub_layout)
        main_layout.addWidget(title_label)

        # Загрузка конфигурации локатора:
        selector_frame = QFrame()
        selector_frame.setStyleSheet(status)
        selector_layout = QHBoxLayout(selector_frame)
        selector_layout.setContentsMargins(0, 0, 0, 0)
        selector_layout.setSpacing(0)

        combo_label = QLabel("Выбрать локатор из списка:")
        combo_label.setStyleSheet(sub_explanations)

        self.avaible_locator_combo = QComboBox()
        self.avaible_locator_combo.setStyleSheet(sub_layout)
        self.avaible_locator_combo.addItems(self.ordered_lctrs)
        self.avaible_locator_combo.setFixedWidth(500)
        self.avaible_locator_combo.currentTextChanged.connect(
            lambda text: self._handle_locator_selection(text, self.lctr_avaible_handler)
        )

        selector_layout.addWidget(combo_label)
        selector_layout.addWidget(self.avaible_locator_combo)
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

        self.download_lctr_combo = QComboBox()
        self.download_lctr_combo.setStyleSheet(sub_layout)
        self.download_lctr_combo.addItems([])
        self.download_lctr_combo.setFixedWidth(450)
        self.download_lctr_combo.currentTextChanged.connect(
            lambda text: self._handle_locator_selection(text, self.lctr_download_handler)
        )

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
        slct_lctr_layout.addWidget(self.download_lctr_combo )
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

        self.parameter_names = [
            "Название локатора:",
            "Тип сигнала:",
            "Рабочий диапазон частот, Гц:",
            "Период повторения импульсов, мкс:",
            "Частота повторения импульсов, Гц:",
            "Длительность импульса, с:",
            "Интервал приема, c:",
            "Интервал покоя, c:",
            "Мощность передатчика в импульсе, Вт:",
            "Средняя мощность передатчика, Вт:",
            "Инструментальная дальность, м:",
            "Разрешающая способность, м:",
            "Точность, м:",
            "Количество импульсов, шт:"
        ]

        parameter_value = self.lctr_avaible_handler.read_locator_characteristics()

        self.edit_widgets = []
        for idx, name in enumerate(self.parameter_names):
            group_frame = QFrame()
            group_frame.setStyleSheet(status)
            group_layout = QHBoxLayout(group_frame)
            group_layout.setContentsMargins(0, 0, 0, 0)

            label = QLabel(name)
            label.setStyleSheet(sub_explanations)
            edit = QLineEdit()

            if idx < len(parameter_value):
                value = parameter_value[idx]
                edit.setText(str(value) if value is not None else "")

            edit.setStyleSheet(sub_layout)
            edit.setFixedSize(200, 30)

            group_layout.addWidget(label)
            group_layout.addWidget(edit)
            lctr_chrtcs_layout.addWidget(group_frame)

            self.edit_widgets.append(edit)

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
        add_button.clicked.connect(self._add_locator)
        add_button.setFixedSize(200, 30)

        # Удаление локатора
        del_lctr_label = QLabel("Удалить текущий локатор из\n общего списка локаторов:")
        del_lctr_label.setStyleSheet(sub_explanations)

        del_button = QPushButton("Удалить")
        del_button.clicked.connect(self._delete_locator)
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
            self.lctr_download_handler = LocatorManagerActionHandler(self.selected_file)
            lctrs_download = self.lctr_download_handler.get_locators()
            ordered_lctrs = ["Выберите элемент"]
            for locator in lctrs_download:
                if locator != "Выберите элемент" and locator not in ordered_lctrs:
                    ordered_lctrs.append(locator)
                self.download_lctr_combo.addItems(ordered_lctrs)

    def _handle_locator_selection(self, selected_text: str, lctr_handler: LocatorManagerActionHandler):
        if selected_text != "Выберите элемент":
            lctr_handler.write_locator_characteristics(selected_text)
            self._write_characteristics_fields(lctr_handler)
        else:
            self._clear_characteristics_fields()

    def _write_characteristics_fields(self, lctr_handler: LocatorManagerActionHandler):
        parameter_value = lctr_handler.read_locator_characteristics()

        for idx, edit in enumerate(self.edit_widgets):
            if idx < len(parameter_value):
                value = parameter_value[idx]
                edit.setText(str(value) if value is not None else "")
    
    def _clear_characteristics_fields(self):
        parameter_value = [None]*14

        for idx, edit in enumerate(self.edit_widgets):
            if idx < len(parameter_value):
                value = parameter_value[idx]
                edit.setText(str(value) if value is not None else "")

    def _add_locator(self):
        previous_locators = set(self.lctr_avaible_handler.get_locators())

        self.lctr_avaible_handler.add_locator()

        new_locators = set(self.lctr_avaible_handler.get_locators())

        added_locators = new_locators - previous_locators

        for locator in added_locators:
            if locator != "Выберите элемент":
                self.ordered_lctrs.append(locator)

        self.avaible_locator_combo.clear()
        self.avaible_locator_combo.addItems(self.ordered_lctrs)
        self.avaible_locator_combo.setCurrentIndex(0)

    def _delete_locator(self):
        self.avaible_locator_combo.clear()

        self.lctr_avaible_handler.delete_locator()

        new_locators = self.lctr_avaible_handler.get_locators()

        ordered_lctrs = ["Выберите элемент"]
        seen = {"Выберите элемент"}

        for locator in new_locators:
            if locator not in seen and locator != "Выберите элемент":
                ordered_lctrs.append(locator)
                seen.add(locator)

        self.avaible_locator_combo.addItems(ordered_lctrs)
        self.avaible_locator_combo.setCurrentIndex(0)

    def _connect_settings(self):
        """Подключение сигналов для автоматического обновления всех настроек"""
        for edit in self.edit_widgets:
            edit.textChanged.connect(self._handle_settings_change)

    def _handle_settings_change(self):
        """Обработчик изменений параметров локатора"""
        # Сопоставление подписей полей с именами параметров модели
        field_mapping = {
            "Название локатора:": "locator",
            "Тип сигнала:": "signal",
            "Рабочий диапазон частот, Гц:": "frequency_range",
            "Период повторения импульсов, мкс:": "pulse_repetition_period",
            "Частота повторения импульсов, Гц:": "pulse_repetition_frequency",
            "Длительность импульса, с:": "pulse_duration",
            "Интервал приема, c:": "reception_interval",
            "Интервал покоя, c:": "rest_interval",
            "Мощность передатчика в импульсе, Вт:": "transmitter_pulse_power",
            "Средняя мощность передатчика, Вт:": "average_transmitter_power",
            "Инструментальная дальность, м:": "instrumental_range",
            "Разрешающая способность, м:": "resolution",
            "Точность, м:": "accuracy",
            "Количество импульсов, шт:": "number_pulse"
        }

        settings_data = {}

        for idx, (name, edit) in enumerate(zip(self.parameter_names, self.edit_widgets)):
            field_name = field_mapping.get(name)
            if not field_name:
                continue
            value = edit.text()

            if field_name in ["locator", "signal"]:
                converted_value = str(value)
            else:
                converted_value = float(value) if value else 0.0

            settings_data[field_name] = converted_value

        self.lctr_avaible_handler.update_locator_characteristics(settings_data)
