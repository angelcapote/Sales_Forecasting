from abc import abstractclassmethod
import pandas as pd
from abc import ABC, abstractmethod


class APredict(ABC):
    def __init__(self, data):
        self.data = data
        self.predicted_data = pd.DataFrame()
        self.predicted = False

    @abstractclassmethod
    def predictSales(self):
        pass

    def isPredicted(self):
        if (self.predicted):
            return True
        else:
            return False

    def resetIndex(self):
        self.predicted_data = self.predicted_data.rename_axis(
            'Fecha Contable').reset_index()
