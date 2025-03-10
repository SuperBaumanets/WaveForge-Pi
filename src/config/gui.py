# Настройки главного окна
window_settings = {
    "window_title": "WaveForge Analyzer",
    "initial_size": (1280, 720),
    "initial_position": (100, 100),
    "minimum_size": (800, 600)
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