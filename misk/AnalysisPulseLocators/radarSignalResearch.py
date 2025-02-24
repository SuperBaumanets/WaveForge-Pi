from src.radarChirpSignal import intraPulseLinearChirp
from src.radarPhaseManipulationSignal import intraPulseQPSK

if __name__ == "__main__":

    # Параметры сигнала для AN/FPS-108
    #Rtarget_ANFPS108 = 1000e3    # Дистанция до цели (м)
    #fc_ANFPS108 = 1175e6         # Начальная частота
    #B_ANFPS108 = 200e6           # Полоса частот
    #tau_ANFPS108 = 1e-6          # Длительность импульса
    #PRF_ANFPS108 = 46            # Частота повторения импульсов
    #N_pulses_ANFPS108 = 2        # Количество импульсов
    #intraPulseLinearChirp(fc_ANFPS108, B_ANFPS108, tau_ANFPS108, PRF_ANFPS108, N_pulses_ANFPS108, Rtarget_ANFPS108)

   
    # Параметры сигнала для MM/SPN-703
    #Rtarget_MMSPN703 = 120e3     # Дистанция до цели (м)
    #fc_MMSPN703 = 9375e6         # Начальная частота
    #B_MMSPN703 = 16.7e6          # Полоса частот
    #tau_MMSPN703 = 1.5e-6        # Длительность импульса
    #PRF_MMSPN703 = 650           # Частота повторения импульсов
    #N_pulses_MMSPN703 = 2        # Количество импульсов
    #intraPulseLinearChirp(fc_MMSPN703, B_MMSPN703, tau_MMSPN703, PRF_MMSPN703, N_pulses_MMSPN703, Rtarget_MMSPN703)

    # Параметры сигнала для S 1810
    Rtarget_S1810= 75e3     # Дистанция до цели (м)
    fc_S1810 = 8600e6       # Начальная частота
    B_S1810 = 10e6          # Полоса частот
    tau_S1810 = 2e-6        # Длительность импульса
    PRF_S1810 = 4000        # Частота повторения импульсов
    N_pulses_S1810 = 2      # Количество импульсов
    intraPulseLinearChirp(fc_S1810, B_S1810, tau_S1810, PRF_S1810, N_pulses_S1810, Rtarget_S1810)

    # Параметры сигнала для TAFLIR
    #Rtarget_TAFLIR= 100e3     # Дистанция до цели (м)
    #fc_TAFLIR = 2900e6        # Начальная частота
    #Chirp_TAFLIR = 4          # Количество чипов
    #tau_TAFLIR = 6.8e-6       # Длительность импульса
    #PRF_TAFLIR = 235          # Частота повторения импульсов
    #N_pulses_TAFLIR = 2       # Количество импульсов
    #intraPulseQPSK(fc_TAFLIR, Chirp_TAFLIR, tau_TAFLIR, PRF_TAFLIR, N_pulses_TAFLIR, Rtarget_TAFLIR)