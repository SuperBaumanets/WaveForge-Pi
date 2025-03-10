import sys
import pyqtgraph as pg
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit,
    QFormLayout, QGroupBox, QMessageBox
)
from PySide6.QtCore import Qt

class MeasurementPlot(pg.PlotWidget):
    def init(self, parent=None):
        super().init(parent)
        self.setBackground('w')
        self.setLabel('left', 'Y Axis')
        self.setLabel('bottom', 'X Axis')
        
        self.v_lines = []
        self.h_lines = []
        
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.plot(x, y, pen='b', name="Signal")

    def create_line(self, angle, color):
        line = pg.InfiniteLine(
            angle=angle, 
            movable=True, 
            pen=pg.mkPen(color, width=2),
            hoverPen=pg.mkPen(color, width=4)
        )
        return line

    def add_vertical_lines(self):
        if len(self.v_lines) == 0:
            line1 = self.create_line(90, '#FF0000')
            line2 = self.create_line(90, '#FF4444')
            self.addItem(line1)
            self.addItem(line2)
            self.v_lines = [line1, line2]
            return True
        return False

    def add_horizontal_lines(self):
        if len(self.h_lines) == 0:
            line1 = self.create_line(0, '#00FF00')
            line2 = self.create_line(0, '#44FF44')
            self.addItem(line1)
            self.addItem(line2)
            self.h_lines = [line1, line2]
            return True
        return False

    def clear_lines(self, line_type):
        if line_type == 'vertical':
            for line in self.v_lines:
                self.removeItem(line)
            self.v_lines = []
        elif line_type == 'horizontal':
            for line in self.h_lines:
                self.removeItem(line)
            self.h_lines = []

class MainWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Измерительные курсоры (2x2)")
        self.setGeometry(100, 100, 1000, 800)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout()
        main_widget.setLayout(layout)
        
        self.plot = MeasurementPlot()
        
        control_panel = QGroupBox("Управление курсорами")
        control_layout = QVBoxLayout()
        
        self.btn_add_v = QPushButton("Добавить вертикальные курсоры")
        self.btn_add_v.clicked.connect(self.add_vertical)
        
        self.btn_add_h = QPushButton("Добавить горизонтальные курсоры")
        self.btn_add_h.clicked.connect(self.add_horizontal)
        
        self.btn_clear_v = QPushButton("Очистить вертикальные")
        self.btn_clear_v.clicked.connect(self.clear_vertical)
        
        self.btn_clear_h = QPushButton("Очистить горизонтальные")
        self.btn_clear_h.clicked.connect(self.clear_horizontal)
        
        self.vLine1_edit = QLineEdit()
        self.vLine2_edit = QLineEdit()
        self.deltaX_edit = QLineEdit()
        self.hLine1_edit = QLineEdit()
        self.hLine2_edit = QLineEdit()
        self.deltaY_edit = QLineEdit()
        
        for edit in [self.vLine1_edit, self.vLine2_edit, self.deltaX_edit,
                    self.hLine1_edit, self.hLine2_edit, self.deltaY_edit]:
            edit.setReadOnly(True)
            edit.setStyleSheet("background-color: #F0F0F0;")
        
        form = QFormLayout()
        form.addRow("Вертикальный 1 (X):", self.vLine1_edit)
        form.addRow("Вертикальный 2 (X):", self.vLine2_edit)
        form.addRow("ΔX:", self.deltaX_edit)
        form.addRow("Горизонтальный 1 (Y):", self.hLine1_edit)
        form.addRow("Горизонтальный 2 (Y):", self.hLine2_edit)
        form.addRow("ΔY:", self.deltaY_edit)
        
        control_layout.addWidget(self.btn_add_v)
        control_layout.addWidget(self.btn_add_h)
        control_layout.addWidget(self.btn_clear_v)
        control_layout.addWidget(self.btn_clear_h)
        control_layout.addLayout(form)
        control_panel.setLayout(control_layout)

        layout.addWidget(control_panel, stretch=1)
        layout.addWidget(self.plot, stretch=4)
        
        # Подключаем обработчики перемещения
        self.plot.scene().sigMouseMoved.connect(self.update_measurements)

    def add_vertical(self):
        if self.plot.add_vertical_lines():
            for line in self.plot.v_lines:
                line.sigPositionChanged.connect(self.update_measurements)
        else:
            QMessageBox.warning(self, "Ошибка", 
                              "Вертикальные курсоры уже добавлены!")

    def add_horizontal(self):
        if self.plot.add_horizontal_lines():
            for line in self.plot.h_lines:
                line.sigPositionChanged.connect(self.update_measurements)
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
            self.vLine1_edit.setText(f"{v1:.3f}")
            self.vLine2_edit.setText(f"{v2:.3f}")
            self.deltaX_edit.setText(f"{v2 - v1:.3f}")
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
            self.deltaY_edit.setText(f"{h2 - h1:.3f}")
        else:
            self.hLine1_edit.clear()
            self.hLine2_edit.clear()
            self.deltaY_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())