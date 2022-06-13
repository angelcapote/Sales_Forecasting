from Predict.APredic import APredict
from statsmodels.tsa.ar_model import AutoReg


class Autoregression(APredict):
    def __init__(self, data):
        super().__init__(data)
        self.start = len(self.data)
        # predict es el numero de meses a predecir

    def predictSales(self, predict):
        self.end = len(self.data)+predict-1
        model = AutoReg(self.data, lags=[1, 11, 12], seasonal=True)
        model_fit = model.fit()
        self.predicted_data = model_fit.predict(
            self.start, self.end).rename("Autoregresión")
