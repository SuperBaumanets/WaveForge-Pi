from PySide6.QtCore import Signal, QObject

class LogSignals(QObject):
    update_log = Signal(str)

class SubTab1ActionHandler:
    _signals = LogSignals()

    @classmethod
    def connect_log_signal(cls, callback):
        cls._signals.update_log.connect(callback)

    @classmethod
    def run_static_emitting(cls):
        print("Функция: Запуск статического излучения")
        cls.write_host_log("SubTab1: Запуск статического излучения")
    
    @classmethod
    def run_dynamic_emitting(cls):
        print("Функция: Запуск динамического излучения")
        cls.write_host_log("SubTab1: Запуск динамического излучения")

    @classmethod
    def stop_emitting(cls):
        print("Функция: Остановка излучения")
        cls.write_host_log("SubTab1: Остановка излучения")

    @classmethod
    def write_host_log(cls, message):
        cls._signals.update_log.emit(message)  # Отправка в GUI