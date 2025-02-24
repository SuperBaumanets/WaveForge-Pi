from PySide6.QtCore import Signal, QObject

class LogSignals(QObject):
    update_log = Signal(str)

class SubTab2ActionHandler:
    _signals = LogSignals()

    @classmethod
    def connect_to_target(cls):
        print("Функция: Подключение к Raspberry")
        cls.write_host_log("SubTab2: Подключение к Raspberry")

        return True

    @classmethod
    def connect_log_signal(cls, callback):
        cls._signals.update_log.connect(callback)

    @classmethod
    def run_static_emitting(cls):
        print("Функция: Запуск статического излучения")
        cls.write_host_log("SubTab2: Запуск статического излучения")
    
    @classmethod
    def run_dynamic_emitting(cls):
        print("Функция: Запуск динамического излучения")
        cls.write_host_log("SubTab2: Запуск динамического излучения")

    @classmethod
    def stop_emitting(cls):
        print("Функция: Остановка излучения")
        cls.write_host_log("SubTab2: Остановка излучения")

    @classmethod
    def write_host_log(cls, message):
        cls._signals.update_log.emit(message)