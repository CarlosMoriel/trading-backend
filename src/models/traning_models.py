import tensorflow as tf
import numpy as np

class traning_model:
    traningData = []
    model = any
    history = any
    
    def __init__(self, model):
        self.model = model
    
    def trainModel(self, inputs, results):
        print("Comenzando entrenamiento...")
        self.history =  self.model.fit(inputs, results, epochs=1000, verbose=False)
        print("Modelo entrenado!")
    