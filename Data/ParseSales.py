from Data.ParseData import ParseData
import pandas as pd
import os


class ParseSales(ParseData):
    def __init__(self, path, name):
        super().__init__(path, name)

    def preprocesData(self):
        self.loadData()
        self.copyData()
        self.setIndex()
        self.groupData()
        self.resetIndex()
        self.deleteToDate("2014-01-31")
        self.setIndex()  # Si no vuelvo a poner la fecha como indice falla autoreg
        # Tengo que resetearlo en Prophet

    def randomForestData(self):
        print("Introduzca el nombre con los datos de random forest.")
        fichero_rf = input()
        os.chdir(self.path)
        os.getcwd()
        self.sales_rf = pd.read_csv(fichero_rf, sep=',')
        # asumo que me la dan con la estructura necesaria

    def randomForestDataPredict(self):
        print("Introduzca el nombre con los datos para predecir el random forest.")
        fichero_rf = input()
        os.chdir(self.path)
        os.getcwd()
        self.predict_rf = pd.read_csv(fichero_rf, sep=',')

    def prophetDataPredict(self):
        print("Introduzca el nombre con los datos para predecir prophet.")
        fichero_pr = input()
        os.chdir(self.path)
        os.getcwd()
        self.predict_prophet = pd.read_csv(fichero_pr, sep=';')

    "Copy the necessary data from the dataset"

    def copyData(self):
        self.parsed_sales["Fecha Contable"] = self.sales["Fecha Contable"]
        self.parsed_sales["Unidades Vendidas"] = self.sales["Unidades Vendidas"]

    def groupData(self):
        self.parsed_sales = self.parsed_sales.resample('M').sum()

    def setIndex(self):
        self.parsed_sales.set_index('Fecha Contable', inplace=True)
        self.parsed_sales.index = pd.to_datetime(
            self.parsed_sales.index, dayfirst='true')

    def resetIndex(self):
        self.parsed_sales = self.parsed_sales.rename_axis(
            'Fecha Contable').reset_index()

    "Deletes from date to the newest"

    def deleteFromDate(self, date):
        indx = self.parsed_sales[self.parsed_sales['Fecha Contable'] > date].index
        self.parsed_sales = self.parsed_sales.drop(indx)

    "Deletes to date"

    def deleteToDate(self, date):
        indx = self.parsed_sales[self.parsed_sales['Fecha Contable'] < date].index
        self.parsed_sales = self.parsed_sales.drop(indx)
