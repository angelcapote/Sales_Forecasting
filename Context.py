import matplotlib.pyplot as plt

from Predict.Autoregression import Autoregression
from Predict.RandomForest import RandomForest
from Predict.Sarima import Sarima
from Predict.Prophet import Prophet_
from Data.ParseData import ParseData
from Data.ParseSales import ParseSales
from Results.Results import Results


class Context():
    # Objeto Parse sales   n_tr y n_pr son los numeros a usar para dividir el df
    def __init__(self, sales, n_train):
        self.sales = sales
        self.sales.preprocesData()
        self.train = sales.parsed_sales.iloc[:n_train, :]
        self.predict = sales.parsed_sales.iloc[n_train:, :]

        self.validate = [Autoregression(self.train), Prophet_(sales.parsed_sales, self.sales), Sarima(self.train), RandomForest(
            sales.parsed_sales, self.sales)]

        self.predictions = [Autoregression(sales.parsed_sales), Prophet_(
            sales.parsed_sales, self.sales), Sarima(sales.parsed_sales), RandomForest(sales.parsed_sales, self.sales)]
        self.predictions[1].predicted = True
        self.predictions[3].predicted = True

    "Validates with all the available methods"

    def validateSales(self):
        for i in self.validate:
            i.predictSales(len(self.predict))

    "Predicts with all the available methods"

    def predictSales(self, months_predict):
        self.months_predict = months_predict
        for i in self.predictions:
            i.predictSales(self.months_predict)
            # self.predictions

    def printPredictions(self):
        for i in self.predictions:
            print(i)
            print(i.predicted_data)

    "Predicts with the specified method"
    # def predictSales(self, method):
    #   if i.name = method: predict
    #   method

    def representSales(self):
        self.predictions[0].data.plot()

    def representPredictions(self):
        self.results.predictions_df.plot()

    def representError(self):
        self.results.predictions_err.plot()

    def representAll(self):
        self.representPredictions()
        self.representError()

    def generateResults(self):
        self.results = Results(self.validate, self)
