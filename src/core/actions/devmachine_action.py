from PySide6.QtCore import Signal, QObject
from src.core.signal_processing.signal_generator import SignalGenerator
from src.core.settings.locator import locator
from src.core.settings.plot import plot_fourier

class LogSignals(QObject):
    update_log = Signal(str)          
    update_plot_signal = Signal(object, object)
    update_plot_fft = Signal(object, object)
    clear_plot_data = Signal()

class RunDevMchnActionHandler:
    _last_generator = None
    _is_model_run = False
    _signals = LogSignals()

    @classmethod
    def connect_log_signal(cls, callback):
        """Подключение обработчика логов"""
        cls._signals.update_log.connect(callback)

    @classmethod
    def connect_plot_signal(cls, callback):
        """Метод для подключения обработчика графика"""
        cls._signals.update_plot_signal.connect(callback)

    @classmethod
    def connect_plot_fft(cls, callback):
        """Метод для подключения обработчика графика"""
        cls._signals.update_plot_fft.connect(callback)

    @classmethod
    def connect_clear_plot(cls, callback):
        """Метод для подключения обработчика графика"""
        cls._signals.clear_plot_data.connect(callback)


    @classmethod
    def run_theory_model(cls):
        """Отправка данных"""
        try:
            if locator.signal == "chirp":
                generator = SignalGenerator(
                    'chirp',
                    locator.frequency_range,
                    10e6,
                    locator.pulse_duration,
                    locator.pulse_repetition_frequency,
                    locator.number_pulse
                )
            else:
                generator = SignalGenerator(
                    'QPSK',
                    locator.frequency_range,
                    4,
                    locator.pulse_duration,
                    locator.pulse_repetition_frequency,
                    locator.number_pulse
                )

            cls._last_generator = generator
            cls._is_model_run = True

            tx_times, tx_signals = generator.get_pulse_sequence()
            cls._signals.update_plot_signal.emit(tx_times, tx_signals)
            cls._update_spectrum()

            cls.write_host_log("Моделирование теоретического сигнала излучения")
        except ValueError as e:
            error_msg = f"Ошибка генерации сигнала - {str(e)}"
            cls.write_host_log(error_msg)

    @classmethod
    def _update_spectrum(cls):
        """Обновление спектра с текущими настройками"""
        if cls._is_model_run and cls._last_generator:
            try:
                freq, spectrum_db = cls._last_generator.get_spectrum(
                    n_fft=plot_fourier.n_fft,
                    window=plot_fourier.window
                )
                cls._signals.update_plot_fft.emit(freq, spectrum_db)
            except Exception as e:
                error_msg = f"Ошибка обновления спектра: {str(e)}"
                cls.write_host_log(error_msg)

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
        """Существующий метод логирования"""
        cls._signals.update_log.emit(message)