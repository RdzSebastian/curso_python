#####################################
###           TP FINAL            ### 
### MIRO FRANCO - DNI: 41.672.314 ###
#####################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn import metrics
from sklearn.linear_model import LinearRegression



filepath = ('C:\\Franco\\Facultad\\Unsam\\Mate 3\\Unsam.Clase.12.4.6.2021\\cvs_para_el_TP\\seguro.csv')

dataset = pd.read_csv(filepath)

print(f'DIMENSION DATASET: {dataset.shape}')
print()
print(f'DESCRIPCION DATASET: ')
print(dataset.describe())
print()
print('COLUMNAS CON ALGUN NaN:')
print(dataset.isnull().any())

#Las variables independiente seran 'age','sex','bmi','children','smoker','region'
X = dataset.iloc[:, :-1].values #Matriz con tamaños
#La variable dependiente sera el 'charges'
y = dataset.iloc[:,6].values #Matriz de pesos

#Traduciendo a dato numerico las columnas 'sex','smoker' y 'region'
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
X[:, 5] = labelencoder_X.fit_transform(X[:, 5])

print(X[:,1])
print(X[:,4])
print(X[:,5])

#Grafico de regresion lineal multiple con los datos iniciales
plt.figure(figsize=(10,10))
plt.tight_layout()
seabornInstance.distplot(dataset['charges'])
plt.show()


#Dividimos los datos en conjunto de entrenamiento y conjunto de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Escalamos los datos
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Se crea el modelo con los datos de entrenamiento
regressor = LinearRegression()
regressor.fit(X_train, y_train)

df = dataset.drop(['charges'], axis=1)
df = df.T
df = df.index

coeff_df = pd.DataFrame(regressor.coef_, df, columns=['Coefficient']) 
print(coeff_df)





























# y_pred = regressor.predict(X_test)

# print('Error Medio Absoluto (MAE):', metrics.mean_absolute_error(y_test, y_pred))
# print('Error cuadrático medio (MSE):', metrics.mean_squared_error(y_test, y_pred))
# print('Raíz cuadrada del error cuadrático medio (RMSE) :', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# dftx = pd.DataFrame(X_train,columns=['X_train'])
# dftx['y_train'] = y_train
# print('MATRIZ CONJ. ENTRENAMIENTO')
# print(dftx)
# print()
# dftxt = pd.DataFrame(X_test,columns=['X_test'])
# dftxt['y_test'] = y_test
# print('MATRIZ CONJ. TEST')
# print(dftxt)
# print()


