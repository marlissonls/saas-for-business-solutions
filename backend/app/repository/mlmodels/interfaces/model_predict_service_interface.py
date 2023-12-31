from abc import ABC, abstractmethod
import pandas as pd
from typing import Any, List

class IPredictService(ABC):

    @abstractmethod
    def __init__(self):
        self.model_dir: str
        self.dataframe: pd.DataFrame
    
    @abstractmethod
    def is_number(self, value: str) -> bool:
        pass

    @abstractmethod
    def preprocessing(self, features: dict) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_model(self, model_path: str) -> Any:
        pass

    @abstractmethod
    def predict_service(self, model_id: str, features: dict) -> List:
        pass