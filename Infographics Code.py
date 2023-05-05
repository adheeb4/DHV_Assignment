# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:07:25 2023

@author: adheeb
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(filename):

    data = pd.read_csv(filename, skiprows=4)
    data_transposed = data.set_index("Country Name").transpose()
    data_transposed = data_transposed.drop(index=["Country Code",
                                                  "Indicator Name",
                                                  "Indicator Code"])
    return data, data_transposed
