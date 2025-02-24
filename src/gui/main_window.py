from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QScrollArea, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from .tabs import Tab1, Tab2, Tab3, Tab4

from src.gui.styles.main_panel import main
from src.gui.styles.left_panel import panel
from src.gui.styles.right_panel import substrate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fixed Size Interface")
        
        # Фиксированные размеры главного окна
        self.setFixedSize(1200, 600)
        self.setStyleSheet(main)
        
        # Главный контейнер
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Горизонтальный layout
        layout = QHBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Левая панель (фиксированная ширина)
        left_panel = QScrollArea()
        left_panel.setFixedWidth(400)
        left_panel.setWidgetResizable(True)
        
        # Контейнер для вкладок
        tabs_container = QWidget()
        tabs_container.setStyleSheet(panel)
        tabs_layout = QVBoxLayout(tabs_container)
        tabs_layout.setContentsMargins(0, 0, 0, 0)  
        tabs_layout.setSpacing(0)                   
        tabs_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Добавление вкладок
        self.tabs = [Tab1(self), Tab2(self), Tab3(self), Tab4(self)]
        for tab in self.tabs:
            tabs_layout.addWidget(tab)
            tab.setContentsMargins(0, 0, 0, 0)  
        
        left_panel.setWidget(tabs_container)
        
        # Правая панель (фиксированные размеры)
        right_panel = QWidget()
        right_panel.setStyleSheet(substrate)
        right_panel.setFixedSize(800, 600)
        
        # Инициализация контента
        self.content_stack = QStackedWidget(right_panel)
        self.content_stack.setGeometry(0, 0, 800, 600)
        self.load_content_pages()
        
        # Добавление панелей в layout
        layout.addWidget(left_panel)
        layout.addWidget(right_panel)

        # Текущий активный подтаб
        self.last_active_subtab = None
        
        # Блокировка изменения размеров
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)

    def load_content_pages(self):
        # Import all subtabs
        from .tabs._tab1.subtab1 import Sub1Tab1Content
        from .tabs._tab1.subtab2 import Sub2Tab1Content
        from .tabs._tab1.subtab3 import Sub3Tab1Content
        from .tabs._tab2.subtab1 import Sub1Tab2Content
        from .tabs._tab3.subtab1 import Sub1Tab3Content
        from .tabs._tab3.subtab2 import Sub2Tab3Content
        from .tabs._tab4.subtab1 import Sub1Tab4Content
        
        # Add all content widgets
        self.content_stack.addWidget(Sub1Tab1Content())
        self.content_stack.addWidget(Sub2Tab1Content())
        self.content_stack.addWidget(Sub3Tab1Content())
        self.content_stack.addWidget(Sub1Tab2Content())
        self.content_stack.addWidget(Sub1Tab3Content())
        self.content_stack.addWidget(Sub2Tab3Content())
        self.content_stack.addWidget(Sub1Tab4Content())

    def show_content(self, index: int):
        self.content_stack.setCurrentIndex(index)

    def set_active_subtab(self, new_subtab):
        # Сбрасываем предыдущий активный подтаб
        if self.last_active_subtab is not None:
            self.last_active_subtab.setChecked(False)
            self.last_active_subtab.setEnabled(True)
        
        # Устанавливаем новый активный подтаб
        new_subtab.setChecked(True)
        new_subtab.setEnabled(False)
        self.last_active_subtab = new_subtab