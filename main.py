from fio import fileIO
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

file = fileIO(r"C:\Users\Mattia Colalongo\OneDrive - Novac SRL\Sharezone\Novac Condivisa\R&D materials\Cartelle_Personali\Mattia_Colalongo\LFP_Gr_ST\graphite_capacity\2C")
file.conversion()
# file.extract_charge()
# file.extract_discharge()

file = fileIO(r"C:\Users\Mattia Colalongo\OneDrive - Novac SRL\Sharezone\Novac Condivisa\R&D materials\Cartelle_Personali\Mattia_Colalongo\LFP_Gr_ST\graphite_capacity\2C\csv")
file.extract_charge()
file.extract_discharge()
