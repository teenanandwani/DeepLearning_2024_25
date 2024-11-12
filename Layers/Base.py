import numpy as np
#from src_to_implement.Optimization import Optimizers


class BaseLayer:
    def __init__(self):
        self.trainable = False
        self.weights = []
