from pydantic import ValidationError
from src.utils.toml_gui_manager import TomlManager
from src.core.settings.locator import locator


class LocatorManagerActionHandler:
    def __init__(self, toml_path: str):
        self.toml_manager = TomlManager(toml_path)

    def get_locators(self) -> list:
        """Возвращает список доступных локаторов"""
        return self.toml_manager.get_table_names()

    def write_locator_characteristics(self, table_name: str) -> bool:
        """Загружает характеристики локатора из TOML"""
        try:
            raw_data = self.toml_manager.read_all_fields(table_name)
            if not raw_data:
                return False

            # Обновляем глобальные настройки
            locator.update_settings({
                "locator": table_name,
                **raw_data
            })
            return True
            
        except ValidationError as e:
            print(f"Ошибка валидации: {e}")
            return False
        except Exception as e:
            print(f"Ошибка загрузки: {str(e)}")
            return False
    
    def update_locator_characteristics(self, settings_data: dict)-> bool:
        """Обновление характеристик локатора"""
        try:    
            locator.update_settings(settings_data)
            return True
        except ValidationError as e:
            error_msg = f"Ошибка валидации настроек: {str(e)}"
            print(error_msg)
            return False
        except Exception as e:
            error_msg = f"Ошибка обновления: {str(e)}"
            print(error_msg)
            return False

    def read_locator_characteristics(self) -> dict:
        """Возвращает характеристики в виде словаря"""
        return [
            getattr(locator, field)
            for field in locator.model_fields.keys()
        ]

    def add_locator(self):
        """Добавляет новый локатор в TOML"""
        try:
            if not locator.locator:
                raise ValueError("Название локатора не может быть пустым")

            table_fields = {
            field: getattr(locator, field)
            for field in locator.model_fields.keys()
            if field != "locator"
        }
            
            if self.toml_manager.read_all_fields(locator.locator):
                raise ValueError(f"Локатор '{locator.locator}' уже существует")
            
            self.toml_manager.add_table(locator.locator, table_fields)
            
        except Exception as e:
            print(f"Ошибка добавления: {str(e)}")

    def delete_locator(self):
        """Удаляет локатор из TOML"""
        try:
            if not locator.locator:
                raise ValueError("Название локатора не может быть пустым")
            
            if not self.toml_manager.read_all_fields(locator.locator):
                raise ValueError(f"Локатор '{locator.locator}' не найден")

            self.toml_manager.delete_table(locator.locator)

        except Exception as e:
            print(f"Ошибка удаления: {str(e)}")