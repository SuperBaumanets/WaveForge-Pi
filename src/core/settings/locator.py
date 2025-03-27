from typing import Dict, Any
from pydantic import BaseModel, ConfigDict, Field

class LocatorSettings(BaseModel):
    locator: str = Field(default="")
    signal: str = Field(default="")
    frequency_range: float = Field(default=0.0)
    pulse_repetition_period: float = Field(default=0.0)
    pulse_repetition_frequency: float = Field(default=0.0)
    pulse_duration: float = Field(default=0.0)
    reception_interval: float = Field(default=0.0)
    rest_interval: float = Field(default=0.0)
    transmitter_pulse_power: float = Field(default=0.0)
    average_transmitter_power: float = Field(default=0.0)
    instrumental_range: float = Field(default=0.0)
    resolution: float = Field(default=0.0)
    accuracy: float = Field(default=0.0)
    number_pulse: float = Field(default=0.0)

    model_config = ConfigDict(
        frozen=False,  
        extra="forbid"
    )

    def update_settings(self, new_data: Dict[str, Any]) -> None:
        valid_fields = self.model_fields.keys()
        filtered_data = {k: v for k, v in new_data.items() if k in valid_fields}
        for key, value in filtered_data.items():
            setattr(self, key, value)

locator = LocatorSettings()