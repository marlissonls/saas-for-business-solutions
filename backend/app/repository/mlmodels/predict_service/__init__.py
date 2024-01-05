from app.repository.mlmodels.interfaces.model_predict_service_interface import IPredictService
from app.repository.mlmodels.interfaces.model_interface import FeatureData, PredictResponse
import joblib
import pandas as pd
from os.path import dirname
from typing import Any, List

MODELS = f'{dirname(__file__)}/models'

class PredictService(IPredictService):

    def __init__(self):
        self.model_dir = MODELS
        self.dataframe = pd.DataFrame


    def is_number(self, value: str) -> bool:
        for char in value:
            if not (char.isdigit() or char == '.'):
                return False
        return True


    def preprocessing(self, features: FeatureData) -> pd.DataFrame:
        features_values = features.features_values
        features_inputs = features.features_template

        for key, value in features_values.items():
            if type(value) == bool:
                features_inputs[key] = [1.0] if value else [0.0]
            elif self.is_number(value):
                features_inputs[key] = [float(value)]
            elif type(value) == str:
                features_inputs[value] = [1.0]

        return self.dataframe(features_inputs)


    def get_model(self, model_path: str) -> Any:
        try:
            model = joblib.load(model_path)
            return model
        except Exception as error:
            raise error


    def predict_service(self, model_id: str, features: dict) -> PredictResponse:
        try:
            model_path = f'{self.model_dir}/{model_id}.pkl'

            model = self.get_model(model_path)

            df_features = self.preprocessing(features)

            target = model.predict(df_features)

            return PredictResponse(
                status=True,
                message='Previsão realizada!',
                data=target
            )

        except Exception as error:
            print('Erro', error)
            return PredictResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )