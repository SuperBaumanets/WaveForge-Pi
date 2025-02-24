
import numpy as np
import pyqtgraph as pg

class MeasurementPlot(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.v_lines = []
        self.h_lines = []
        self.x_data = np.array([])
        self.y_data = np.array([])
        
        self.setBackground('w')
        self.setLabel('left', '', units='')
        self.setLabel('bottom', ' ', units=' ')
        self.showGrid(x=True, y=True, alpha=0.3)
        
        self.curve = self.plot(pen=pg.mkPen(color='b', width=2), name="Сигнал")

    def create_line(self, angle, color):
        line = pg.InfiniteLine(
            angle=angle, 
            movable=True, 
            pen=pg.mkPen(color, width=1, dash=[4, 2]),
            hoverPen=pg.mkPen('#000000', width=1, dash=[4, 2]))
        return line
    
    def add_vertical_lines(self):
        if not self.v_lines:
            line1 = self.create_line(90, '#6D6D6D')
            line2 = self.create_line(90, '#6D6D6D')
            self.addItem(line1)
            self.addItem(line2)
            self.v_lines = [line1, line2]
            return True
        return False

    def add_horizontal_lines(self):
        if not self.h_lines:
            line1 = self.create_line(0, '#6D6D6D')
            line2 = self.create_line(0, '#6D6D6D')
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

    def update_plot_data(self, x, y):
        self.x_data = np.asarray(x)
        self.y_data = np.asarray(y)
        self.curve.setData(self.x_data, self.y_data)

    def append_plot_data(self, new_x, new_y):
        self.x_data = np.append(self.x_data, new_x)
        self.y_data = np.append(self.y_data, new_y)
        self.curve.setData(self.x_data, self.y_data)

    def clear_plot_data(self):
        self.x_data = np.array([])
        self.y_data = np.array([])
        self.curve.setData([], [])