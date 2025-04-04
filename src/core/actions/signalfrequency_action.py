from pydantic import ValidationError
from src.core.settings.plot import plot_fourier

class LocatorManagerActionHandler:
    def write_plot_settings(self, settings_data: dict) -> bool:
        """Обновление настроек графика"""
        try:
            if 'n_fft' in settings_data:
                settings_data['n_fft'] = int(settings_data['n_fft'])
                
            plot_fourier.update_settings(settings_data)
            return True
        except ValidationError as e:
            error_msg = f"Ошибка валидации настроек: {str(e)}"
            print(error_msg)
            return False
        except Exception as e:
            error_msg = f"Ошибка обновления: {str(e)}"
            print(error_msg)
            return False

    def read_plot_settings(self) -> dict:
        """Чтение текущих настроек"""
        return {
            "window": plot_fourier.window,
            "n_fft": plot_fourier.n_fft
        }