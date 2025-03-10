import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

matplotlib.use('TkAgg')

def intraPulseQPSK(fc: float,   # Несущая частота (Гц)
                 B: int,       # Количество чипов на импульс
                 tau: float,   # Длительность импульса (с)
                 PRF: float,   # Частота повторения импульсов (Гц)
                 N_pulses: int, # Количество импульсов
                 R_target: float):  # Дистанция до цели (м)
    
    c = 3e8
    T_pri = 1 / PRF
    t_delay = 2 * R_target / c

    # Параметры модуляции
    n_chips = B
    chip_duration = tau / n_chips

    # Автоматический расчет частоты дискретизации
    B_signal = n_chips / tau  # Теоретическая полоса сигнала
    f_max = fc + B_signal/2
    nyquist_rate = 2 * f_max
    fs = nyquist_rate * 1.1  # Запас 10% выше Найквиста
    # Ограничение минимальной частоты дискретизации для коротких импульсов
    if fs < 10e9:
        fs = 10e9

    # Генерация QPSK сигнала
    def generate_pulse_segment(start_time, is_tx=True):
        t_segment = np.arange(start_time, start_time + tau, 1/fs)
        t_local = t_segment - start_time
        
        # Генерация фаз QPSK
        np.random.seed(42)
        phases = np.random.choice([0, np.pi/2, np.pi, 3*np.pi/2], n_chips)
        
        signal = np.zeros_like(t_local)
        for i in range(n_chips):
            t_start = i * chip_duration
            t_end = (i+1) * chip_duration
            mask = (t_local >= t_start) & (t_local < t_end)
            signal[mask] = np.sin(2*np.pi*fc*t_local[mask] + phases[i])
            
        return t_segment, signal * (0.5 if not is_tx else 1.0)

    # Генерация сигналов
    tx_times, tx_signals = [], []
    rx_times, rx_signals = [], []
    
    for n in range(N_pulses):
        tx_start = n * T_pri
        t_tx, s_tx = generate_pulse_segment(tx_start)
        tx_times.append(t_tx)
        tx_signals.append(s_tx)
        
        rx_start = tx_start + t_delay
        t_rx, s_rx = generate_pulse_segment(rx_start, is_tx=False)
        rx_times.append(t_rx)
        rx_signals.append(s_rx)

    # Создание отдельных графиков
    fig1, ax1 = plt.subplots(figsize=(12, 4))
    fig2, ax2 = plt.subplots(figsize=(12, 4))
    fig3, ax3 = plt.subplots(figsize=(12, 4))
    
    # График 1: Форма импульса
    ax1.plot(tx_times[0]*1e6, tx_signals[0], 'b', lw=1.5)
    ax1.set_title('Форма QPSK импульса')
    ax1.set(xlabel='Время (мкс)', ylabel='Амплитуда', 
           xlim=(0, tau*1e6*1.1))
    
    # График 2: Последовательность импульсов
    for t_tx, s_tx in zip(tx_times, tx_signals):
        ax2.plot(t_tx*1e3, s_tx, 'navy')
    ax2.set_title('Последовательность импульсов')
    ax2.set(xlabel='Время (мс)', ylabel='Амплитуда', 
           xlim=(0, N_pulses*T_pri*1e3))
    
    # График 3: Спектр сигнала
    N_fft = 2097152
    spectrum = fftshift(fft(tx_signals[0], N_fft))
    freq = fftshift(np.fft.fftfreq(N_fft, 1/fs))
    spectrum_db = 20*np.log10(np.abs(spectrum)/np.max(np.abs(spectrum)) + 1e-12)
    ax3.plot(freq/1e6, spectrum_db, 'darkgreen')
    ax3.set_title('Спектр QPSK сигнала')
    ax3.set(xlabel='Частота (МГц)', ylabel='Мощность (дБ)',
           xlim=((fc - B_signal)/1e6, (fc + B_signal)/1e6))
        
    # Настройка сетки для всех графиков
    for ax in [ax1, ax2, ax3]:
        ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.show()