from Predict.APredic import APredict
import pandas as pd
from prophet import Prophet


class Prophet_(APredict):
    def __init__(self, data, sales):
        super().__init__(data)
        self.sales = sales
        self.data = self.data.rename_axis(
            'Fecha Contable').reset_index()
        self.data = self.data.rename(columns={'Fecha Contable': 'ds',
                                              'Unidades Vendidas': 'y'})

    def predictSales(self, predict):
        if self.isPredicted():
            self.sales.prophetDataPredict()
            pre = self.sales.predict_prophet
        else:
            # Estoy cambiandolo para dejar solo un año en la validación
            pred_ = self.data.iloc[60:, :]
            pre = pd.DataFrame()
            pre['ds'] = pred_['ds']
            self.data = self.data.iloc[:60, :]

        m = Prophet()
        m.fit(self.data)
        forecast = m.predict(pre)
        self.predicted_data['Fecha Contable'] = forecast['ds']
        self.predicted_data['Prophet'] = forecast['yhat']

        self.predicted_data.set_index('Fecha Contable', inplace=True)
        self.predicted_data.index = pd.to_datetime(self.predicted_data.index)
        self.predicted = True
