import os


class fileIO:
    """
    Class which handles BTS layer reports excel files. python-calamine library is required for speeding up rading process 
    """
    def __init__(self, filepath):
        self.path = filepath
        self.dict = {}
        self.family = input("Insert group family to split data the data:").split(",")
        for j in self.family:
            self.list = []
            for i in os.listdir(self.path):
                if (".xlsx" in i) and (j in i):
                    self.list.append(i)
            self.dict[f"{j.replace("-","")}"] = self.list