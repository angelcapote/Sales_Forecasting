from Predict.APredic import APredict
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


class RandomForest(APredict):
    def __init__(self, data, sales):
        super().__init__(data)
        self.target = pd.DataFrame()
        self.features = pd.DataFrame()
        self.sales = sales

        self.sales.randomForestData()
        self.sales_rftmp = self.sales.sales_rf.copy()
        self.target = self.sales_rftmp['Unidades Vendidas']
        self.features = self.sales.sales_rf.copy()
        self.features = self.features.drop('Unidades Vendidas', axis=1)

    def predictSales(self, predict):
        if self.isPredicted():
            self.sales.randomForestDataPredict()
            pred_feat = self.sales.predict_rf  # son las features
        else:
            # Estoy cambiandolo para dejar solo un año en la validación

            pred_t = self.target.iloc[48:]
            self.target = self.target.iloc[:48]
            pred_feat = self.features.iloc[48:]
            self.features = self.features.iloc[:48]  # entrenamiento

        # Instantiate model with 1000 decision trees
        rf = RandomForestRegressor(n_estimators=1000, random_state=42)
        # Train the model on training data
        rf.fit(self.features, self.target)

        predict_rrf = rf.predict(pred_feat)

        self.data = self.data.iloc[60:]
        self.data.loc[:, 'Random forest'] = predict_rrf
        self.data = self.data.drop('Unidades Vendidas', axis=1)

        self.predicted_data['Random Forest'] = self.data
        self.predicted = True
