# WaveForge-Pi

waveforge_pi/                  # Корневая директория проекта
├── docs/                      # Документация
│   └── setup_guide.md         # Инструкции по настройке Raspberry Pi
├── pi_examples/               # Примеры C-кода для Raspberry Pi
│   └── signal_generator.c     # Тестовый код для генерации сигнала на GPIO
├── src/                       # Исходный код приложения
│   ├── core/                  # Логика генерации и анализа сигналов
│   │   ├── signal_generator.py
│   │   └── fft_analyzer.py
│   ├── gui/                   # Графический интерфейс
│   │   ├── main_window.py     # Основное окно приложения
│   │   ├── signal_list.py     # Виджет списка сигналов
│   │   └── plots.py           # Графики (время/частота)
│   ├── utils/                 # Вспомогательные модули
│   │   ├── ssh_client.py      # Работа с SSH (Paramiko)
│   │   ├── file_manager.py    # Сохранение/загрузка сигналов (JSON/SQLite)
│   │   └── exceptions.py      # Кастомные исключения
│   └── config/                # Конфигурации
│       └── settings.py        # Настройки приложения (пути, параметры Pi)
├── tests/                     # Тесты
│   ├── test_signal_generator.py
│   └── test_ssh_client.py
├── main.py                    # Точка входа в приложение
├── requirements.txt           # Зависимости (numpy, paramiko и т.д.)
└── README.md                  # Описание проекта и инструкции