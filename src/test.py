import tensorflow as tf
import numpy as np
from binance.client import Client
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

binance_client = Client('CDmG49sRfS3pXUMChi5itOH0f6elIW0frAvizDDpuE0UCYJRt1pccggO7JXhWfYv', 
            '8trKMxv8WjS3tn04QNycWY6RSVNULkwE0HfDtYm5cKk9rQHYwm4URyGGhcHCbF5i')
 
initial_date = "2 Jan, 2023"
finish_date = "3 Jan, 2023"
pair_coin = 'BNBBTC'
kandle_interval = '1h'

predict_array = binance_client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)
numberOfKandlesPredict = len(predict_array)


initial_date = "1 Apr, 2022"
finish_date = "1 Jan, 2023"
pair_coin = 'BNBBTC'
kandle_interval = '1h'

mainArray = binance_client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)
numberOfKandles = len(mainArray)

inputs = []
results = []

if numberOfKandles % 2 > 0:
    numberOfKandles -= 1



# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(10,6)),  # capa de entrada: aplanar la matriz de entrada
    tf.keras.layers.Dense(50, activation='relu'), # primera capa oculta
    tf.keras.layers.Dense(50, activation='relu'), # segunda capa oculta
    tf.keras.layers.Dense(50, activation='relu'), # tercera capa oculta
    tf.keras.layers.Dense(1, activation='sigmoid') # capa de salida
])

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

flag = True
while(flag):
    if(numberOfKandles % 11 > 0):
        numberOfKandles -= 1
    else:
        flag = False

arrayInput = []
arrayOutput = []

count = 0
internalArray = []
for i in range(numberOfKandles):
    if(count < 10):
        internalArray.append([float(mainArray[i][1]),
                              float(mainArray[i][2]),
                              float(mainArray[i][3]),
                              float(mainArray[i][4]),
                              float(mainArray[i][5]),
                              float(mainArray[i][8])])
        count += 1
    else:
        arrayInput.append(internalArray)
        if(internalArray[0][0] < float(mainArray[i][4])):
            arrayOutput.append([1])
        else:
            arrayOutput.append([0])
        internalArray = []
        count = 0
        
    
print(arrayInput[0])
print(arrayOutput[0])
print('---------------------')

# entrenar el modelo
history = model.fit(arrayInput, arrayOutput, epochs=500, batch_size=32, verbose=True)

plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(history.history["loss"]) 
plt.show()

result = model.predict([[[0.014771, 0.014773, 0.014738, 0.014754, 575.8, 839.0], [0.014755, 0.01478, 0.014753, 0.014779, 786.631, 1065.0], [0.01478, 0.014793, 0.01475, 0.01477, 795.261, 1051.0], [0.01477, 0.014774, 0.014742, 0.01476, 1238.817, 1198.0], [0.014761, 0.014776, 0.014731, 0.014762, 821.267, 1100.0], [0.014761, 0.014776, 0.014729, 0.01473, 749.267, 1079.0], [0.01473, 0.014755, 0.014728, 0.014751, 451.025, 727.0], [0.014751, 0.014761, 0.014741, 0.014745, 451.49, 782.0], [0.014745, 0.014745, 0.014723, 0.014737, 606.633, 1058.0], [0.014738, 0.01478, 0.014737, 0.01478, 679.219, 950.0]]])
print(result) 
model.save('keras_model.h5')


