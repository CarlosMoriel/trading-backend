import tensorflow as tf
import numpy as np
from binance.client import Client
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

binance_client = Client('CDmG49sRfS3pXUMChi5itOH0f6elIW0frAvizDDpuE0UCYJRt1pccggO7JXhWfYv', 
            '8trKMxv8WjS3tn04QNycWY6RSVNULkwE0HfDtYm5cKk9rQHYwm4URyGGhcHCbF5i')
 
# Crear el modelo
model = Sequential()

# Agregar una capa de entrada con 12 neuronas y una capa de salida con 2 neuronas
model.add(Dense(12, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='relu'))

# Compilar el modelo
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

initial_date = "11 Apr, 2022"
finish_date = "12 Apr, 2022"
pair_coin = 'BNBBTC'
kandle_interval = '1h'

predict_array = binance_client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)


initial_date = "1 Apr, 2022"
finish_date = "2 Apr, 2022"
pair_coin = 'BNBBTC'
kandle_interval = '1h'

mainArray = binance_client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)
numberOfKandles = len(mainArray)

print(mainArray)

inputs = []
results = []

if numberOfKandles % 2 > 0:
    numberOfKandles -= 1

count = 0
arrayInput = np.array([[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12]])


for n in range(numberOfKandles):
    if(count < 3):
        arrayInput[0][0].append(float(mainArray[n][0]))
        arrayInput[1].append(float(mainArray[n][1]))
        arrayInput[2].append(float(mainArray[n][2]))
        arrayInput[3].append(float(mainArray[n][3]))
        arrayInput[4].append(float(mainArray[n][4]))
        arrayInput[5].append(float(mainArray[n][5]))
        arrayInput[6].append(float(mainArray[n][6]))
        arrayInput[7].append(float(mainArray[n][7]))
        arrayInput[8].append(float(mainArray[n][8]))
        arrayInput[9].append(float(mainArray[n][9]))
        arrayInput[10].append(float(mainArray[n][10]))
        arrayInput[11].append(float(mainArray[n][11]))
        count += 1
    else:
        count = 0
        inputs.append([arrayInput[0]])
        arrayInput = [[],[],[],[],[],[],[],[],[],[],[],[]]
        results.append([float(i) for i in mainArray[n]])
       
            
print(inputs)
print('----------') 
print(results) 
history = model.fit(inputs, results, epochs=500, verbose=False)
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(history.history["loss"]) 
plt.show()

model.save('    keras_model.h5')
x = [float(i) for i in predict_array[10]]
y = [float(i) for i in predict_array[11]]
print(x)
print(y)
result = model.predict([x])
print(result)