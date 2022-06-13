import pandas as pd


class Results():
    def __init__(self, predictions, context):
        self.predictions = predictions
        self.predictions_df = pd.DataFrame(context.predict)
        self.mergePredictions()
        self.predictions_err = pd.DataFrame(self.predictions_df)
        self.calculateError()
        self.results = pd.DataFrame()
        # self.mergeAll()

    def calculateError(self):
        self.predictions_err['Error_autoreg%'] = (abs(
            self.predictions_df['Unidades Vendidas'] - self.predictions_df.iloc[:, 1])*100)/self.predictions_df['Unidades Vendidas']
        self.predictions_err['Error_sarima%'] = (abs(
            self.predictions_df['Unidades Vendidas'] - self.predictions_df.iloc[:, 2])*100)/self.predictions_df['Unidades Vendidas']

        self.predictions_err['Error_Prophet%'] = (abs(
            self.predictions_df['Unidades Vendidas'] - self.predictions_df.iloc[:, 3])*100)/self.predictions_df['Unidades Vendidas']
        self.predictions_err['Error_RandomForest%'] = (abs(
            self.predictions_df['Unidades Vendidas'] - self.predictions_df.iloc[:, 4])*100)/self.predictions_df['Unidades Vendidas']
        #self.predictions_err['Error_Media%'] = (abs(self.predictions_df['Unidades Vendidas'] - self.predictions_df['Media Predicciones'])*100)/self.predictions_df['Unidades Vendidas']

    def mergePredictions(self):
        # print(self.predictions[0].predicted_data)
        self.predictions_df = pd.merge(
            self.predictions_df, self.predictions[0].predicted_data, left_index=True, right_index=True, how='left')
        self.predictions_df = pd.merge(
            self.predictions_df, self.predictions[1].predicted_data, left_index=True, right_index=True, how='left')
        self.predictions_df = pd.merge(
            self.predictions_df, self.predictions[2].predicted_data, left_index=True, right_index=True, how='left')
        self.predictions_df = pd.merge(
            self.predictions_df, self.predictions[3].predicted_data, left_index=True, right_index=True, how='left')
        #self.predictions_df = pd.merge(self.predictions_df, self.predictions[1].predicted_data, left_on='Fecha Contable', right_on='Fecha Contable', how='left')

    def mergeAll(self):
        self.results = pd.merge(
            self.results, self.predictions_err, left_index=True, right_index=True, how='left')
