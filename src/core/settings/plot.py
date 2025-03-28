from typing import Dict, Any
from pydantic import BaseModel, ConfigDict, Field

class PlotSettings(BaseModel):
    window: str | None = Field(default=None)
    n_fft: int = Field(default=2097152)
    
    model_config = ConfigDict(
        frozen=False,  
        extra="forbid"
    )

    def update_settings(self, new_data: Dict[str, Any]) -> None:
        valid_fields = self.model_fields.keys()
        filtered_data = {k: v for k, v in new_data.items() if k in valid_fields}
        for key, value in filtered_data.items():
            setattr(self, key, value)

plot_fourier = PlotSettings()