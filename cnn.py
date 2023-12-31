# Cargar el conjunto de datos
import pandas as pd
from sklearn.preprocessing import StandardScaler
dataset=pd.read_csv("heart.csv")

#standardScaler = StandardScaler()
#columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
#dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])
# Dividir el conjunto de datos en características (X) y etiquetas (y)
X=dataset.iloc[:,0:13]
y=dataset.iloc[:,13:14]

# Dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)
# Escalar los datos
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)


from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout

# Crear el modelo secuencial
model = Sequential()

# Capa oculta 1 con capa de entrada
model.add(Dense(units=145,activation="relu",input_dim=13))

# Capa oculta 2
model.add(Dense(units=120,activation="relu",))

#3rd hidden layer
model.add(Dense(units=70,activation="relu",))



# Capa de salida
model.add(Dense(units=1,activation="sigmoid"))

model.summary()
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model_his=model.fit(X_train,y_train,validation_split=0.30, batch_size=55,epochs=25,verbose=1)


y_pred=model.predict(X_test)
y_pred = (y_pred > 0.45)


from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)
print(score)

from sklearn.metrics import confusion_matrix,classification_report
cm = confusion_matrix(y_test, y_pred)
print(cm)


print(classification_report(y_test,y_pred))


import matplotlib.pyplot as plt
# Graficar la precisión del modelo
plt.plot(model_his.history['accuracy'])
plt.plot(model_his.history['val_accuracy'])
plt.title('Precisión del modelo')
plt.ylabel('Precisión')
plt.xlabel('Época')
plt.legend(['Entrenamiento', 'Prueba'], loc='upper left')
plt.show()


# summarize history for loss
plt.plot(model_his.history['loss'])
plt.plot(model_his.history['val_loss'])
plt.title('Precisión del modelo')
plt.ylabel('Precisión')
plt.xlabel('Época')
plt.legend(['Entrenamiento', 'Prueba'], loc='upper left')
plt.show()


# Guardar el modelo (descomenta la siguiente línea si deseas guardar el modelo)
#model.save("heart.h5")