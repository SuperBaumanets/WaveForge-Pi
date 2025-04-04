from PySide6.QtWidgets import (
    QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit,
    QMessageBox, QFrame, QLabel, QScrollArea
)

from src.gui.styles.left_panel import subtab
from src.gui.tabs.styles.subtab import main_layout, sub_layout, sub_explanations, status

from src.gui.plot import MeasurementPlot
from src.core.actions.devmachine_action import RunDevMchnActionHandler

class Sub1Tab3Button(QPushButton):
    def __init__(self, index, main_window, main_tab_id):
        super().__init__("Теоретический излучаемый сигнал")
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

class Sub1Tab3Content(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        RunDevMchnActionHandler.connect_plot_signal(self.update_plot)
    
    def _setup_ui(self):
        self.setObjectName("container")
        layout = QVBoxLayout(self)
        self.title = QLabel("Теоретический излучаемый сигнал")
        self.title.setStyleSheet(subtab)

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
        control_panel = self._create_control_panel()
        scroll_layout.addWidget(control_panel)
        
        # Настраиваем скролл
        scroll.setWidget(scroll_content)
        main_frame_layout.addWidget(scroll)

        # Добавляем основной контейнер в главный layout
        main.addWidget(main_frame)
        return main

    def _create_control_panel(self):
        frame = QFrame()
        frame.setStyleSheet(sub_layout)
        layout = QVBoxLayout(frame)

        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        cursor_control_frame = QFrame()
        cursor_control_frame.setStyleSheet(sub_layout)
        cursor_control_layout = QVBoxLayout(cursor_control_frame)
        cursor_control_layout.setContentsMargins(0, 0, 0, 0)
        cursor_control_layout.setSpacing(0)

        control_panel_title = QLabel("Управление курсорами")
        control_panel_title.setStyleSheet(sub_layout)
        
        self.btn_add_v = QPushButton("Добавить вертикальные\n курсоры")
        self.btn_add_v.clicked.connect(self.add_vertical)
        self.btn_add_v.setStyleSheet("font-size: 12px;")

        self.btn_clear_v = QPushButton("Очистить вертикальные\nкурсоры")
        self.btn_clear_v.clicked.connect(self.clear_vertical)
        self.btn_clear_v.setStyleSheet("font-size: 12px;")
        
        self.btn_add_h = QPushButton("Добавить горизонтальные\n курсоры")
        self.btn_add_h.clicked.connect(self.add_horizontal)
        self.btn_add_h.setStyleSheet("font-size: 12px;")
        
        self.btn_clear_h = QPushButton("Очистить горизонтальные\n курсоры")
        self.btn_clear_h.clicked.connect(self.clear_horizontal)
        self.btn_clear_h.setStyleSheet("font-size: 12px;")

        vLine1_edit_layout = QHBoxLayout()
        vLine1_edit_label = QLabel("Курсор 1 по оси X:")
        vLine1_edit_label.setStyleSheet(sub_explanations)
        self.vLine1_edit = QLineEdit()
        vLine1_edit_layout.addWidget(vLine1_edit_label)
        vLine1_edit_layout.addWidget(self.vLine1_edit)

        vLine2_edit_layout = QHBoxLayout()
        vLine2_edit_label = QLabel("Курсор 2 по оси X:")
        vLine2_edit_label.setStyleSheet(sub_explanations)
        self.vLine2_edit = QLineEdit()
        vLine2_edit_layout.addWidget(vLine2_edit_label)
        vLine2_edit_layout.addWidget(self.vLine2_edit)

        deltaX_edit_layout = QHBoxLayout()
        deltaX_edit_label = QLabel("Дельта X:")
        deltaX_edit_label.setStyleSheet(sub_explanations)
        self.deltaX_edit = QLineEdit()
        deltaX_edit_layout.addWidget(deltaX_edit_label)
        deltaX_edit_layout.addWidget(self.deltaX_edit)

        hLine1_edit_layout = QHBoxLayout()
        hLine1_edit_label = QLabel("Курсор 1 по оси Y:")
        hLine1_edit_label.setStyleSheet(sub_explanations)
        self.hLine1_edit = QLineEdit()
        hLine1_edit_layout.addWidget(hLine1_edit_label)
        hLine1_edit_layout.addWidget(self.hLine1_edit)

        hLine2_edit_layout = QHBoxLayout()
        hLine2_edit_label = QLabel("Курсор 2 по оси Y:")
        hLine2_edit_label.setStyleSheet(sub_explanations)
        self.hLine2_edit = QLineEdit()
        hLine2_edit_layout.addWidget(hLine2_edit_label)
        hLine2_edit_layout.addWidget(self.hLine2_edit)

        deltaY_edit_layout = QHBoxLayout()
        deltaY_edit_label = QLabel("Дельта Y:")
        deltaY_edit_label.setStyleSheet(sub_explanations)
        self.deltaY_edit = QLineEdit()
        deltaY_edit_layout.addWidget(deltaY_edit_label)
        deltaY_edit_layout.addWidget(self.deltaY_edit)
        
        for edit in [self.vLine1_edit, self.vLine2_edit, self.deltaX_edit,
                    self.hLine1_edit, self.hLine2_edit, self.deltaY_edit]:
            edit.setReadOnly(True)
            edit.setStyleSheet(sub_layout)

        cursor_control_layout.addWidget(control_panel_title)
        cursor_control_layout.addWidget(self.btn_add_v)
        cursor_control_layout.addWidget(self.btn_clear_v)
        cursor_control_layout.addLayout(vLine1_edit_layout)
        cursor_control_layout.addLayout(vLine2_edit_layout)
        cursor_control_layout.addLayout(deltaX_edit_layout)
        cursor_control_layout.addWidget(self.btn_add_h)
        cursor_control_layout.addWidget(self.btn_clear_h)
        cursor_control_layout.addLayout(hLine1_edit_layout)
        cursor_control_layout.addLayout(hLine2_edit_layout)
        cursor_control_layout.addLayout(deltaY_edit_layout)
        cursor_control_layout.addStretch()


        plot_frame = QFrame()
        plot_frame.setStyleSheet(sub_layout)
        plot_layout = QVBoxLayout(plot_frame)
        plot_layout.setContentsMargins(0, 0, 0, 0)
        plot_layout.setSpacing(15)

        plot_title = QLabel("График")
        plot_layout.addWidget(plot_title)

        self.plot = MeasurementPlot()
        self.plot.setFixedHeight(460)  
        self.plot.setFixedWidth(750)
        plot_layout.addWidget(self.plot)
        
        content_layout.addWidget(cursor_control_frame)
        content_layout.addWidget(plot_frame)
        layout.addWidget(content_widget)

        return frame
    
    def add_vertical(self):
        if self.plot.add_vertical_lines():
            for line in self.plot.v_lines:
                line.sigPositionChanged.connect(self.update_measurements)
            self.update_measurements()
        else:
            QMessageBox.warning(self, "Ошибка", 
                               "Вертикальные курсоры уже добавлены!")

    def add_horizontal(self):
        if self.plot.add_horizontal_lines():
            for line in self.plot.h_lines:
                line.sigPositionChanged.connect(self.update_measurements)
            self.update_measurements()
        else:
            QMessageBox.warning(self, "Ошибка",
                               "Горизонтальные курсоры уже добавлены!")

    def clear_vertical(self):
        self.plot.clear_lines('vertical')
        self.update_measurements()

    def clear_horizontal(self):
        self.plot.clear_lines('horizontal')
        self.update_measurements()

    def update_measurements(self):
        # Вертикальные измерения
        if len(self.plot.v_lines) == 2:
            v1 = min(line.value() for line in self.plot.v_lines)
            v2 = max(line.value() for line in self.plot.v_lines)
            self.vLine1_edit.setText(f"{v1 * 1e3:.3f}")
            self.vLine2_edit.setText(f"{v2 * 1e3:.3f}")
            self.deltaX_edit.setText(f"{abs(v2 - v1) * 1e3:.3f}")
        else:
            self.vLine1_edit.clear()
            self.vLine2_edit.clear()
            self.deltaX_edit.clear()
        
        # Горизонтальные измерения
        if len(self.plot.h_lines) == 2:
            h1 = min(line.value() for line in self.plot.h_lines)
            h2 = max(line.value() for line in self.plot.h_lines)
            self.hLine1_edit.setText(f"{h1:.3f}")
            self.hLine2_edit.setText(f"{h2:.3f}")
            self.deltaY_edit.setText(f"{abs(h2 - h1):.3f}")
        else:
            self.hLine1_edit.clear()
            self.hLine2_edit.clear()
            self.deltaY_edit.clear()
    
    def update_plot(self, x_data, y_data):
        self.plot.clear_plot_data()
        self.plot.append_plot_data(x_data, y_data)