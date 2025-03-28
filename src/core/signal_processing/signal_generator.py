import numpy as np
from numpy.fft import fft, fftshift

class SignalGenerator:
    def __init__(self,
                 modulation_type: str, # 'chirp' или 'QPSK'
                 fc: float,            # Несущая частота [Гц]
                 param: float,         # Параметр (B для chirp, чипы для QPSK)
                 tau: float,           # Длительность импульса [с]
                 PRF: float,           # Частота повторения импульсов [Гц]
                 N_pulses: int,        # Количество импульсов
                 seed: int = None):    # Seed для генерации случайных чисел
                
        self.modulation_type = modulation_type
        self.fc = fc
        self.param = param
        self.tau = tau
        self.PRF = PRF
        self.N_pulses = N_pulses
        self.T_pri = 1 / PRF
        self.seed = seed
        
        self.rng = np.random.default_rng(seed)
        
        self.fs = self._calculate_sampling_rate()
        self._validate_parameters()
        
        self.tx_times, self.tx_signals = self._generate_pulses()

    def _validate_parameters(self):
        """Проверка корректности входных параметров"""
        if self.modulation_type not in ["chirp", 'QPSK']:
            raise ValueError("Неподдерживаемый тип модуляции")
        
        if self.modulation_type == 'QPSK' and not isinstance(self.param, int):
            raise ValueError("Для QPSK параметр должен быть целым числом (чипы)")

    def _calculate_sampling_rate(self):
        """Вычисление частоты дискретизации"""
        if self.modulation_type == 'chirp':
            B = self.param
            nyquist_rate = 2 * (self.fc + B)
        elif self.modulation_type == 'QPSK':
            n_chips = self.param
            B_signal = n_chips / self.tau
            nyquist_rate = 2 * (self.fc + B_signal/2)
        else:
            raise ValueError(f"Неподдерживаемый тип модуляции: {self.modulation_type}")

        fs = nyquist_rate * 1.5  
        return max(fs, 200e9)

    def _generate_pulse_segment(self, start_time):
        """Генерация одного импульса"""
        t_segment = np.arange(start_time, start_time + self.tau, 1/self.fs)
        t_local = t_segment - start_time
        
        if self.modulation_type == 'chirp':
            signal = self._generate_chirp(t_local)
        elif self.modulation_type == 'QPSK':
            signal = self._generate_qpsk(t_local)
        else:
            signal = np.zeros_like(t_local)
            
        return t_segment, signal

    def _generate_chirp(self, t_local):
        """Генерация ЛЧМ сигнала (возвращает только сигнал)"""
        B = self.param
        return np.sin(2 * np.pi * (self.fc * t_local + 0.5 * (B/self.tau) * t_local**2))

    def _generate_qpsk(self, t_local):
        """Генерация QPSK сигнала (возвращает только сигнал)"""
        n_chips = int(self.param)
        chip_duration = self.tau / n_chips
        phases = self.rng.choice([0, np.pi/2, np.pi, 3*np.pi/2], size=n_chips)
        
        signal = np.zeros_like(t_local)
        for i, phase in enumerate(phases):
            t_start = i * chip_duration
            t_end = (i+1) * chip_duration
            mask = (t_local >= t_start) & (t_local < t_end)
            signal[mask] = np.sin(2*np.pi*self.fc*t_local[mask] + phase)
            
        return signal

    def _generate_pulses(self):
        """Генерация последовательности импульсов"""
        tx_times, tx_signals = [], []
        for n in range(self.N_pulses):
            start_time = n * self.T_pri
            t, s = self._generate_pulse_segment(start_time)
            tx_times.append(t)
            tx_signals.append(s)
        return tx_times, tx_signals

    def get_pulse_sequence(self):
        """Возвращает данные импульсов с разрывами для визуализации"""
        full_t = np.array([], dtype=float)
        full_s = np.array([], dtype=float)

        for t_seg, s_seg in zip(self.tx_times, self.tx_signals):
            full_t = np.concatenate([full_t, t_seg])
            full_s = np.concatenate([full_s, s_seg])

            full_t = np.concatenate([full_t, [np.nan]])
            full_s = np.concatenate([full_s, [np.nan]])

        return full_t[:-1], full_s[:-1]

    def get_spectrum(self, n_fft=2097152, window=None):
        """Возвращает данные спектра для первого импульса"""
        signal = self.tx_signals[0].copy()
    
        if window is not None:
            if not hasattr(np, window):
                raise ValueError(f"Оконная функция {window} не поддерживается")

            win = getattr(np, window)(len(signal))
            signal = signal * win
            signal /= np.mean(win)

        spectrum = fftshift(fft(signal, n_fft))
        freq = fftshift(np.fft.fftfreq(n_fft, 1/self.fs))
        spectrum_db = 20 * np.log10(np.abs(spectrum)/np.max(np.abs(spectrum)) + 1e-12)

        return freq, spectrum_db