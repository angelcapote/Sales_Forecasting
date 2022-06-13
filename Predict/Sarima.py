from Predict.APredic import APredict
from statsmodels.tsa.statespace.sarimax import SARIMAX


# Puedo hacer una funcion que retorne el valor de ajuste que necesito y que la persona lo tenga q pasar a mano a la prediccion


class Sarima(APredict):
    def __init__(self, data):
        super().__init__(data)
        self.start = len(self.data)

    def predictSales(self, predict):
        self.end = len(self.data)+predict-1
        self.predicted_data = 0
        print("Inserte 1 a 1 varlores para SARIMA")
        #model = SARIMAX(self.data, order = (0, 1, 2), seasonal_order = (0, 1, 1, 12))
        model = SARIMAX(self.data,
                        order=(int(input()), int(input()), int(input())),
                        seasonal_order=(int(input()), int(input()), int(input()), int(input())))
        result = model.fit()
        self.predicted_data = result.predict(self.start, self.end,
                                             typ='levels').rename("SARIMA")
