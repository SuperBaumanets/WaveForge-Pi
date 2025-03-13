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
            border: 2px solid #bdc2c7;
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }
        QTabBar::tab:selected {
            background: #A9A9A9;
            color: #0d6efd;
            border: none;
            border-top: 2px solid #0d6efd;
            border-right: 2px solid #0d6efd;  
            border-left: 2px solid #0d6efd;    
        }
        QTabBar::tab:hover {
            background: #bdc2c7;
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
