from abc import ABC, abstractclassmethod, abstractmethod
import pandas as pd
import os


class ParseData(ABC):
    def __init__(self, path, name):
        self.sales = pd.DataFrame()
        self.parsed_sales = pd.DataFrame()
        self.path = path
        self.name = name
        self.sales_rf = pd.DataFrame()
        self.predict_rf = pd.DataFrame()
        self.predict_prophet = pd.DataFrame()

    def loadData(self):
        os.chdir(self.path)
        os.getcwd()
        self.sales = pd.read_csv(self.name, sep=';')

    @abstractclassmethod
    def preprocesData(self):
        pass

    def downloadData(self, down_path):
        self.parsed_sales.to_csv(down_path, sep=';', index=False)
