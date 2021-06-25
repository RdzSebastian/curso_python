#Elijo el dataset 'calcium'
#Variable dependiente = 'cal'
#Varialble independiente = 'time'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:/Users/Ariel/Desktop/Python/TP Final/calcium.csv', usecols= ['time','cal'])
print(dataset)

#Separo en X los datos de Tiempo y en Y los datos de Calcio
X = dataset.iloc[:,0].values
Y = dataset.iloc[:,1].values

print("Tiempo: ", X)
print("Calcio: ", Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=0)

print("X_Train: ", X_train)
print("X_Test: ", X_test)
print("Y_Train: ", Y_train)
print("Y_Test: ", Y_test)

#Escalar los datos para asignar rangos similares a todos los valores
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

#Como estoy trabajando con vectores utilizo '.reshape' para convertirlo en Matriz y usarlo como argumento para 'transform'. Luego utilizo 'squeeze' para volverlo a vector
X_train = np.squeeze(sc_X.fit_transform(X_train.reshape(-1, 1)))
X_test = np.squeeze(sc_X.transform(X_test.reshape(-1,1)))

sc_Y = StandardScaler()
Y_train = np.squeeze(sc_Y.fit_transform(Y_train.reshape(-1, 1)))
Y_test = np.squeeze(sc_Y.transform(Y_test.reshape(-1,1)))

print("X_Train escalado: ", X_train)
print("X_Test escalado: ", X_test)
print("Y_Train escalado: ", Y_train)
print("Y_Test escalado: ", Y_test)


#Regresión linear simple

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train.reshape(-1,1),Y_train.reshape(-1,1))
Y_pred = regression.predict(X_test.reshape(-1,1))

#Gráfico de entrenamiento
df = pd.DataFrame({'Actual': Y_test.flatten(), 'Predicción': Y_pred.flatten()})
plt.scatter(X_train, Y_train, color = "#FF6347")
plt.plot(X_train, regression.predict(X_train.reshape(-1,1)), color = "#20B2AA")
plt.title("Calcio a través del tiempo (Conjunto de Entrenamiento)")
plt.xlabel("Tiempo")
plt.ylabel("Calcio")
plt.show()

#Gráfico de testing
plt.scatter(X_test, Y_test, color = "#FF6347")
plt.plot(X_train, regression.predict(X_train.reshape(-1,1)), color = "#20B2AA")
plt.title("Calcio a través del tiempo (Conjunto de Testing)")
plt.xlabel("Tiempo")
plt.ylabel("Calcio")
plt.show()

#Métricas de gráficos
from sklearn import metrics

print("Error Medio Absoluto (MAE): ", metrics.mean_absolute_error(Y_test, Y_pred))
print("Error cuadrático medio (MSE): ", metrics.mean_squared_error(Y_test, Y_pred))
print("Raíz cuadrada del error cuadrático medio (RMSE): ", np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))

#Conclusión

"""
Se puede observar una relación entre el tiempo transcurrido y un aumento de calcio hasta llegar a un pico en el tiempo promedio.
Una vez que se observa la segunda mitad del tiempo transcurrido, la medida del calcio puede ser mayor o menor según el momento,
pero siempre por encima del valor obtenido a la mitad del estudio.
Se puede observar que tanto en el conjunto de entrenamiento como en el conjunto de testing se obtienen una equidad de valores
por encima y por debajo de la mitad, si se tiene en cuenta desde el comienzo hasta el final del estudio.
"""