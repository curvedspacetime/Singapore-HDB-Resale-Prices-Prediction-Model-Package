from typing import Any, List, Optional

# import numpy as np
from pydantic import BaseModel
from regression_model.processing.validation import HouseDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "town": "ANG MO KIO",
                        "flat_type": "3 ROOM",
                        "storey_range": "01 TO 03",
                        "floor_area_sqm": 67.0,
                        "flat_model": "New Generation",
                        "lease_commence_date": 1980,
                        "remaining_lease": "62 years 05 months",
                        "dist_school": 0.6186,
                        "dist_mrt": 1.0719,
                        "dist_supermarket": 0.8603,
                        "dist_hawker": 0.5924,
                        "dist_npc": 1.1823,
                        "dist_central": 9.8927,
                        "id": 2,
                    }
                ]
            }
        }
