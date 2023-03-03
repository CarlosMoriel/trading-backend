import tensorflow as tf
import numpy as np
from binance.client import Client
import matplotlib.pyplot as plt

class model:
    numberOfShapes = 4
    unitsPerShape = 12
    shapes = []
    model = any
    
    def __init__(self, numberOfShapes):
        self.numberOfShapes = numberOfShapes
        shapes = self.initShapes(self.numberOfShapes , self.unitsPerShape)
        self.initModel(shapes)
        
    def initShapes(self, numberOfShapes, unitsPerShape):
        shapesArray = []
        count = 0
        for i in range(numberOfShapes):
            if count == 0: #If it's the first shape we need put the input shapes
                shapesArray.append(tf.keras.layers.Dense(units=unitsPerShape, input_shape=[1]))
            elif count == (len(shapesArray)-1) : #If it's the final/result shape
                shapesArray.append(tf.keras.layers.Dense(units=2))
            else: #If it's a hiden shape
                shapesArray.append(tf.keras.layers.Dense(units=unitsPerShape))
            count += 1
        return shapesArray
        
    def initModel(self, shapesArray):
        self.model = tf.keras.Sequential(shapesArray)
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )
        
    def exportModel(self, modelName):
        self.model.save(modelName + '.h5')
    
    def inportModel(self, modelName):
        self.model =  tf.keras.models.load_model(modelName + '.h5')
    
    def trainModel(self):
        print('Entrenando modelo')
        binance_client = Client('CDmG49sRfS3pXUMChi5itOH0f6elIW0frAvizDDpuE0UCYJRt1pccggO7JXhWfYv', 
            '8trKMxv8WjS3tn04QNycWY6RSVNULkwE0HfDtYm5cKk9rQHYwm4URyGGhcHCbF5i')
    
        initial_date = "1 Apr, 2022"
        finish_date = "2 Apr, 2022"
        pair_coin = 'BNBBTC'
        kandle_interval = '1h'
        
        mainArray = binance_client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)
        numberOfKandles = len(mainArray)
        
        inputs = []
        results = []
        
        if numberOfKandles % 2 > 0:
            numberOfKandles -= 1
        
        for i in range(numberOfKandles):
            if i % 2 > 0:
                results.append(mainArray[i])
            else:
                inputs.append(mainArray[i])
        
        print(inputs)
        
        history = self.model.fit(inputs, results, epochs=50, verbose=False)
        plt.xlabel("# Epoca")
        plt.ylabel("Magnitud de pérdida")
        plt.plot(history.history["loss"]) 
        
print('Initialize model')
modelo = model(4)
modelo.trainModel()
