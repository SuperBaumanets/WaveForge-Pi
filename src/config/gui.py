# Настройки главного окна
window_settings = {
    "window_title": "WaveForge Analyzer"
}

# Настройки вкладок
tab_settings = {
    "styles": """
        QTabWidget {
            background: #f8f9fa;
            border: none;
        }
        QTabBar::tab {
            min-width: 120px;
            min-height: 40px;
            padding: 8px 15px;
            margin: 0;
            font: 14px "Segoe UI";
            color: #495057;
            background: #e9ecef;
            border: 1px solid #dee2e6;
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }
        QTabBar::tab:selected {
            background: #fff;
            color: #0d6efd;
            border-color: #0d6efd;
        }
        QTabBar::tab:hover {
            background: #dee2e6;
        }
    """,
    "document_mode": True,
    "tabs": [
        {"title": "Подключение\nRaspberry Pi", "widget": "ConnectionTab"},
        {"title": "Локаторы\nи измерения", "widget": "LocatorTab"},
        {"title": "Сигнал\nво временной области", "widget": "SigTimeTab"},
        {"title": "Анализ\nв частотной области", "widget": "SigFreqTab"}
    ]
}

connection_panel = """
    QFrame {
        background-color: #495FFF;
        border: none
        border-radius: 0px;
        padding: 0px;
    }    
    QLabel {
        color: #fff0ff;
        font-size: 12px;
        margin: 0;
        padding: 0;
    }
    QLineEdit, QTextEdit {
        background-color: #333;
        color: #fff;
        border: 1px solid #555;
        padding: 5px;
    }
    QPushButton {
        background-color: #444;
        color: #fff;
        border: 1px solid #555;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #555;
    }
    QCheckBox {
        color: #fff;
    }
"""

connection_panel_title = """
    QLabel {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        margin: 0;
        padding: 0px;
        border: none;
        border-bottom: 2px solid #dee2e6;  
        border-radius: 0px;
    }
"""

status_indicator_connected = "background-color: #00ff00; border-radius: 10px; border: 1px solid #fff;"
status_indicator_disconnected = "background-color: #ff0000; border-radius: 10px; border: 1px solid #fff;"

strim_panel = """
    QFrame {
        background-color: #495057;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 10px;
    }
"""