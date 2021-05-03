from pydantic import BaseModel
class PredictionSystem(BaseModel):
    Pregnancies: int
    Glucose: int
    BMI: float
    Age: int