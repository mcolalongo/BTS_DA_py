import os
import pandas as pd
import numpy as np

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


    def conversion(self):
        self.create_dir("csv")
        for key,values in self.dict.items():
            for i in values:
                self.df = pd.read_excel(os.path.join(self.path, f"{i}"), sheet_name=3, engine='calamine')
                self.df.to_csv(os.path.join(self.path,f"csv/{i}.csv"), sep=',', index=False)
                print(f"File {i}.csv created in csv folder")

    def create_dir(self, folpath):
        self.folpath = folpath
        if os.path.isdir(os.path.join(self.path,self.folpath)):
            print("The folder Exists")
        else:
            print("The folder Doesn't exists, creating...")
            os.mkdir(os.path.join(self.path,self.folpath))


    def extract_charge(self):
        self.create_dir(r"charge")    
        for key,values in self.dict.items():
            for i in values:
                self.df = pd.read_csv(os.path.join(self.path, f"{i}"))
                self.df_filter = self.df.loc[self.df["State"] == "CC Chg"]["Steps"].to_numpy()
                for n in np.unique(self.df_filter):
                    self.filtered = self.df.loc[(self.df["State"] == "CC Chg") & (self.df["Steps"] == n)]
                    self.filtered.to_csv(os.path.join(self.path,f"charge\\{i}_charge_step_{n}.csv"))
                    
                
    def extract_discharge(self):
        self.create_dir(r"discharge")    
        for key,values in self.dict.items():
            for i in values:
                self.df = pd.read_csv(os.path.join(self.path, f"{i}"))
                self.df_filter = self.df.loc[self.df["State"] == "CC DChg"]["Steps"].to_numpy()
                for n in np.unique(self.df_filter):
                    self.filtered = self.df.loc[(self.df["State"] == "CC DChg") & (self.df["Steps"] == n)]
                    self.filtered.to_csv(os.path.join(self.path,f"discharge\\{i}_discharge_step_{n}.csv"))
                    
                

    # def extract_discharge(self):        
    #     for key,values in self.dict.items():
    #         for i in values:
    #             self.df = pd.read_excel(os.path.join(self.path, f"{i}"), sheet_name=3, engine='calamine')
    #             # self.df_filter = self.df.loc[self.df["State"] == "CC DChg"]["Steps"].to_numpy()
    #             # print(np.unique(self.df_filter))