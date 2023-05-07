# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:07:25 2023

@author: adheeb
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def read_data(filename):

    data = pd.read_csv(filename, skipfooter=5, engine='python')
    data_transposed = data.set_index("Country Name").transpose()
    data_transposed = data_transposed.drop(index=["Series Name"])
    return data, data_transposed


Countries_list = ["United Kingdom", "China", "United States",
                  "India", "Indonesia", "Thailand", "Bangladesh"]

electricity_access, electricity_access_t = read_data('Access to electricity (% of population).csv')
co2_emission, co2_emission_t = read_data('CO2 emissions (metric tons per capita).csv')
electricity_hydro, electricity_hydro_t = read_data('electricity_production_hydro.csv')
electricity_hydro_t = electricity_hydro_t[:17]
electricity_nonrenewable, electricity_nonrenewable_t = read_data('electricity_production_nonrenewable.csv')
electricity_nonrenewable_t = electricity_nonrenewable_t[:17]
electricity_nuclear, electricity_nuclear_t = read_data('electricity_production_nuclear.csv')
electricity_renewable, electricity_renewable_t = read_data('electricity_production_renewable.csv')
'''
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))


for i in range(len(Countries_list)):
    ax[0, 0].plot(electricity_access_t.index, electricity_access_t[Countries_list[i]], label=Countries_list[i])
    ax[0, 0].tick_params(axis='x', rotation=90)
    '''
plt.figure()

plt.plot(electricity_hydro_t.index, electricity_hydro_t["India"], electricity_nonrenewable_t["India"])
#ax.yaxis.set_ticks(np.arange(0, 2047, 32))
plt.xticks(rotation=90)
plt.show()