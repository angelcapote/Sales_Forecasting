from Context import Context
from Data.ParseSales import ParseSales
from Predict.Autoregression import Autoregression


def switch():
    print("1. Hacer una predicción.")
    print("2. Imprimir el resultado de las validaciones.")
    print("3. Salir")
    print("Elige una:")
    option = int(input())
    if option == 1:
        print("Inserte el número de meses a predecir:")
        context.predictSales(int(input()))
        print("Resultado de las predicciones: ")
        context.printPredictions()
        switch()
    elif option == 2:
        print(context.results.predictions_df)
        switch()
    elif option == 3:
        print("Hasta luego!")
    else:
        print("Introduzca una opción válida")
        switch()


print("Programa de predicción")
print("Inserte la ruta del archivo: ")
path = input()
print("Inserte el nombre del archivo: ")
name = input()
data = ParseSales(path, name)
#data = ParseSales("/Users/angelcapote/Downloads/TFG/CSV") /Users/angelcapote/Downloads/TFG/CSV3
context = Context(data, 60)


context.validateSales()
context.generateResults()
switch()
