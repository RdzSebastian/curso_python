import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('<ruta de archivo>/Datos_de_salarios.csv')

X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 1].values

print(dataset.shape)
print(dataset.describe())

dataset.plot(x='AniosExperiencia', y='Salario', style='o')
plt.title('Salario vs Años de Experiencia') 
plt.ylabel('Salario') 
plt.xlabel('Años de Experiencia') 
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)


y_pred = regression.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicción': y_pred.flatten()})

plt.scatter(X_train, y_train, color = '#FF6347')
plt.plot(X_train, regression.predict(X_train), color = '#20B2AA')
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo")
plt.show()

plt.scatter(X_test, y_test, color = '#FF6347')
plt.plot(X_train, regression.predict(X_train), color = '#20B2AA')
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo")
plt.show()

from sklearn import metrics
print('Error Medio Absoluto (MAE):', metrics.mean_absolute_error(y_test, y_pred))  
print('Error cuadrático medio (MSE):', metrics.mean_squared_error(y_test, y_pred, squared=True))  
print('Error cuadrático medio de raíz (RMSE):', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

