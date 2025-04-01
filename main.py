from fio import fileIO
import pandas as pd
import os
import matplotlib.pyplot as plt

file = fileIO(r"C:\Users\Mattia Colalongo\OneDrive - Novac SRL\Sharezone\Novac Condivisa\R&D materials\Cartelle_Personali\Mattia_Colalongo\LFP_Gr_ST\graphite_capacity")
print(file.dict)

fig, ax = plt.subplots()
for key,values in file.dict.items():
    for i in values:
        df = pd.read_excel(os.path.join(file.path, f"{i}"), sheet_name=3, engine='calamine')
        df_filter = df.loc[df["State"] == "CC Chg"]
        ax.plot(df_filter["Capacity(Ah)"],df_filter["Voltage(V)"])

plt.savefig(os.path.join(file.path,"s.png"), format='png', dpi=500)

        
        
