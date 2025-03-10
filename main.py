import sys
import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QFormLayout,
    QGroupBox,
    QComboBox
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение с 4 вкладками")
        self.setGeometry(100, 100, 800, 600)
        
        # Создаем виджет с вкладками
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Создаем и добавляем вкладки
        self.create_tab1()  # Информационная вкладка
        self.create_tab2()  # График
        self.create_tab3()  # Настройки
        self.create_tab4()  # О программе

    def create_tab1(self):
        """Первая вкладка - Главная"""
        tab = QWidget()
        main_layout = QVBoxLayout(tab)

        # Верхний блок: Текст + поле ввода
        input_layout = QHBoxLayout()
        input_label = QLabel("Введите параметр:")
        self.main_input = QLineEdit()
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.main_input)
        main_layout.addLayout(input_layout)

        # Блок индикации
        indicator_layout = QHBoxLayout()
        status_label = QLabel("Статус:")
        self.red_indicator = QLabel()
        self.green_indicator = QLabel()

        # Настройка индикаторов
        for ind in [self.red_indicator, self.green_indicator]:
            ind.setFixedSize(20, 20)
            ind.setStyleSheet("border-radius: 10px; border: 1px solid black;")

        self.red_indicator.setStyleSheet("background-color: red;")
        self.green_indicator.setStyleSheet("background-color: #00ff00;")

        indicator_layout.addWidget(status_label)
        indicator_layout.addWidget(self.red_indicator)
        indicator_layout.addWidget(self.green_indicator)
        indicator_layout.addStretch()
        main_layout.addLayout(indicator_layout)

        # Две кнопки в ряд
        button_layout = QHBoxLayout()
        self.left_button = QPushButton("Левая кнопка")
        self.right_button = QPushButton("Правая кнопка")
        button_layout.addWidget(self.left_button)
        button_layout.addWidget(self.right_button)
        main_layout.addLayout(button_layout)

        # Группы параметров
        groups_layout = QHBoxLayout()

        # Левая группа
        left_group = QGroupBox("Левая панель")
        left_layout = QVBoxLayout()
        left_top_label = QLabel("Верхний текст слева")
        self.left_button = QPushButton("Кнопка слева")
        left_bottom_label = QLabel("Нижний текст слева")

        left_layout.addWidget(left_top_label)
        left_layout.addWidget(self.left_button)
        left_layout.addWidget(left_bottom_label)
        left_group.setLayout(left_layout)

        # Правая группа
        right_group = QGroupBox("Правая панель")
        right_layout = QVBoxLayout()
        right_top_label = QLabel("Верхний текст справа")
        self.right_button = QPushButton("Кнопка справа")
        right_bottom_label = QLabel("Нижний текст справа")

        right_layout.addWidget(right_top_label)
        right_layout.addWidget(self.right_button)
        right_layout.addWidget(right_bottom_label)
        right_group.setLayout(right_layout)

        groups_layout.addWidget(left_group)
        groups_layout.addWidget(right_group)
        main_layout.addLayout(groups_layout)
    
        self.tabs.addTab(tab, "Главная")

    def create_tab2(self):
        """Вторая вкладка - График"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Создаем график
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setLabel('left', 'Y значение')
        self.plot_widget.setLabel('bottom', 'X значение')
        self.plot_curve = self.plot_widget.plot(pen='b')
        
        # Генерируем начальные данные
        self.x = np.linspace(0, 10, 100)
        self.y = np.sin(self.x)
        self.plot_curve.setData(self.x, self.y)
        
        layout.addWidget(self.plot_widget)
        self.tabs.addTab(tab, "График")

    def create_tab3(self):
        """Третья вкладка - Настройки"""
        tab = QWidget()
        main_layout = QHBoxLayout(tab)
        
        # Группа параметров
        settings_group = QGroupBox("Параметры графика")
        form_layout = QFormLayout()
        
        self.freq_input = QLineEdit("1.0")
        self.amp_input = QLineEdit("1.0")
        self.color_combo = QComboBox()
        self.color_combo.addItems(["Синий", "Красный", "Зеленый"])
        
        form_layout.addRow("Частота:", self.freq_input)
        form_layout.addRow("Амплитуда:", self.amp_input)
        form_layout.addRow("Цвет:", self.color_combo)
        
        settings_group.setLayout(form_layout)
        
        # Кнопки управления
        btn_group = QGroupBox("Управление")
        btn_layout = QVBoxLayout()
        
        self.btn_update = QPushButton("Обновить график")
        self.btn_reset = QPushButton("Сбросить настройки")
        
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch()
        
        btn_group.setLayout(btn_layout)
        
        # Соединяем сигналы
        self.btn_update.clicked.connect(self.update_plot)
        self.btn_reset.clicked.connect(self.reset_settings)
        
        main_layout.addWidget(settings_group)
        main_layout.addWidget(btn_group)
        self.tabs.addTab(tab, "Настройки")

    def create_tab4(self):
        """Четвертая вкладка - О программе"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        info_text = """
        <h3>О программе</h3>
        <p>Версия: 1.0.0</p>
        <p>Разработчик: Ваша компания</p>
        <p>Лицензия: MIT</p>
        <p>© 2024 Все права защищены</p>
        """
        
        label = QLabel(info_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label)
        self.tabs.addTab(tab, "О программе")

    def update_plot(self):
        """Обновление графика"""
        try:
            freq = float(self.freq_input.text())
            amp = float(self.amp_input.text())
        except ValueError:
            return
        
        color = {
            "Синий": '#2980b9',
            "Красный": '#c0392b',
            "Зеленый": '#27ae60'
        }[self.color_combo.currentText()]
        
        self.y = amp * np.sin(freq * self.x)
        self.plot_curve.setData(self.x, self.y, pen=color)

    def reset_settings(self):
        """Сброс настроек"""
        self.freq_input.setText("1.0")
        self.amp_input.setText("1.0")
        self.color_combo.setCurrentIndex(0)
        self.update_plot()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())