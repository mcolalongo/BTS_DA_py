import pandas as pd
import os


class fileIO:
    """
    Class which handles BTS layer reports excel files. python-calamine library is required for speeding up rading process 
    """
    def __init__(self, filepath):
        self.path = filepath
        self.list = []
        for i in os.listdir(self.path):
            if ".xlsx" in i:
                self.list.append(i)
        
