# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:07:25 2023

@author: adheeb
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.image import imread


def read_data(filename):

    data = pd.read_csv(filename, skipfooter=5, engine='python')
    data_transposed = data.set_index("Country Name").transpose()
    data_transposed = data_transposed.drop(index=["Series Name"])
    return data, data_transposed

Countries_list = ["United Kingdom", "China", "United States",
                  "India", "Thailand", "Bangladesh"]

def mean(data_frame, country):
    mean = np.mean(data_frame[country])
    
    return mean

def median(data_frame, country):
    median = np.median(data_frame[country[i]])

    return median


co2_emission, co2_emission_t = read_data('CO2 emissions (metric tons per capita).csv')
co2_emission_t = co2_emission_t[:18]
co2_emission_t = co2_emission_t.apply(pd.to_numeric)

electricity_hydro, electricity_hydro_t = read_data('electricity_production_hydro.csv')
electricity_hydro_t = electricity_hydro_t[:18]
electricity_hydro_t = electricity_hydro_t.apply(pd.to_numeric)

electricity_nonrenewable, electricity_nonrenewable_t = read_data('electricity_production_nonrenewable.csv')
electricity_nonrenewable_t = electricity_nonrenewable_t[:18]
electricity_nonrenewable_t = electricity_nonrenewable_t.apply(pd.to_numeric)

electricity_nuclear, electricity_nuclear_t = read_data('electricity_production_nuclear.csv')
electricity_nuclear_t = electricity_nuclear_t[:18]
electricity_nuclear_t = electricity_nuclear_t.apply(pd.to_numeric)

electricity_renewable, electricity_renewable_t = read_data('electricity_production_renewable.csv')
electricity_renewable_t = electricity_renewable_t[:18]
electricity_renewable_t = electricity_renewable_t.apply(pd.to_numeric)

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(30, 16))
plt.subplots_adjust(hspace=0.3)

for i in range(len(Countries_list)):
    ax[0,0].plot(co2_emission_t.index, co2_emission_t[Countries_list[i]])
    ax[0,0].set_title("CO\N{SUBSCRIPT TWO} emissions (metric tons per capita)", size=20)
    ax[0,0].set_xticklabels(co2_emission_t.index, rotation=90)
    ax[0,0].grid(True)
    ax[0,0].set_xlabel("Year", size=16)
    ax[0,0].set_ylabel("CO\N{SUBSCRIPT TWO} Emission\n (metric tons per capita)", size=16)
    
for i in range(len(Countries_list)):
    ax[0,1].plot(electricity_hydro_t.index, electricity_hydro_t[Countries_list[i]])
    ax[0,1].set_title("Electricity production from \nhydroelectric sources (% of total)", size=20)
    ax[0,1].set_xticklabels(electricity_hydro_t.index, rotation=90)
    ax[0,1].grid(True)
    ax[0,1].set_xlabel("Year", size=16)
    ax[0,1].set_ylabel("Electricity production from \nhydroelectric sources (% of total)", size=16)

for i in range(len(Countries_list)):
    ax[0,2].plot(electricity_nonrenewable_t.index, electricity_nonrenewable_t[Countries_list[i]])
    ax[0,2].set_title("Electricity production from\n oil, gas and coal sources (% of total)", size=20)
    ax[0,2].set_xticklabels(electricity_nonrenewable_t.index, rotation=90)
    ax[0,2].grid(True)
    ax[0,2].set_xlabel("Year", size=16)
    ax[0,2].set_ylabel("Electricity production from \noil, gas and coal sources (% of total)", size=16)
    
for i in range(len(Countries_list)):
    ax[1,0].plot(electricity_nuclear_t.index, electricity_nuclear_t[Countries_list[i]])
    ax[1,0].set_title("Electricity production from\n nuclear sources (% of total)", size=20)
    ax[1,0].set_xticklabels(electricity_nuclear_t.index, rotation=90)
    ax[1,0].grid(True)
    ax[1,0].set_xlabel("Year", size=16)
    ax[1,0].set_ylabel("Electricity production from\n nuclear sources (% of total)", size=16)
    
for i in range(len(Countries_list)):
    ax[1,1].plot(electricity_renewable_t.index, electricity_renewable_t[Countries_list[i]])
    ax[1,1].set_title("Electricity production from renewable sources,\n excluding hydroelectric (% of total)", size=20)
    ax[1,1].set_xticklabels(electricity_renewable_t.index, rotation=90)
    ax[1,1].grid(True)
    ax[1,1].set_xlabel("Year", size=16)
    ax[1,1].set_ylabel("Electricity production from renewable sources,\n excluding hydroelectric (% of total)", size=16)


ax[1,2].remove()
ax_legend = fig.add_subplot(2, 2, 4)
ax[0,0].legend(Countries_list, fontsize=23, bbox_to_anchor=(3.17,-0.4))
ax_legend.axis('off')

plt.savefig("image1.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure()
mean_co2_list = [np.mean(co2_emission_t["United Kingdom"]),
                 np.mean(co2_emission_t["China"]),
                 np.mean(co2_emission_t["United States"]),
                 np.mean(co2_emission_t["India"]),
                 np.mean(co2_emission_t["Thailand"]),
                 np.mean(co2_emission_t["Bangladesh"])]
                 
plt.barh(Countries_list, mean_co2_list)
plt.ylabel("Countries")
plt.xlabel("CO\N{SUBSCRIPT TWO} Emission(metric tons per capita)")
plt.savefig("image2.png", dpi=300, bbox_inches="tight")
plt.show()


mean_data_us = [np.mean(electricity_hydro_t["United States"]), 
                np.mean(electricity_nonrenewable_t["United States"]),
                np.mean(electricity_nuclear_t["United States"]),
                np.mean(electricity_renewable_t["United States"])]
plt.figure()
plt.pie(mean_data_us, autopct="%1.1f%%")
plt.legend(bbox_to_anchor=(1,1) , 
           labels=["Hydroelectric sources",
                   "Oil, gas and coal sources", 
                   "Nuclear sources", 
                   "Renewable sources, \nexcluding hydroelectric"])
plt.savefig("image3.png", dpi=300, bbox_inches="tight")
plt.show()

dfi_us = pd.DataFrame(co2_emission_t.index)
df1_us = pd.DataFrame(co2_emission_t["United States"]).rename(columns={"United States": "CO2 Emission"})
df2_us = pd.DataFrame(electricity_hydro_t["United States"]).rename(columns={"United States": "Electricity Production(Hydro)"})
df3_us = pd.DataFrame(electricity_nonrenewable_t["United States"]).rename(columns={"United States": "Electricity Production(Non Renewable)"})
df4_us = pd.DataFrame(electricity_nuclear_t["United States"]).rename(columns={"United States": "Electricity Production(Nuclear)"})
df5_us = pd.DataFrame(electricity_renewable_t["United States"]).rename(columns={"United States": "Electricity Production(Renewable)"})

data_us= pd.concat([dfi_us, df1_us, df2_us, df3_us, df4_us, df5_us], axis=1)
data_us.drop(data_us.index[:18], inplace=True)
data_us.drop(data_us.columns[0], axis=1, inplace=True)

plt.figure()
corr = data_us.corr()
sns.heatmap(corr, annot=True, linewidths=0, square=True, cmap='Blues')
plt.savefig("image4.png", dpi=300, bbox_inches="tight")

plt.show()


fig = plt.figure(figsize=(6, 10))
grid = gridspec.GridSpec(3, 2, figure=fig, wspace=0.1, hspace=0.1)

image1 = imread('image1.png')
image2 = imread('image2.png')
image3 = imread('image3.png')
image4 = imread('image4.png')

subplot1 = plt.subplot(grid[0, :])
subplot1.imshow(image1)
subplot1.axis('off')
subplot1.set_title("Comparison of CO2 Emissions and Electricity Production\n in Different Countries")

subplot2 = plt.subplot(grid[1, 0])
subplot2.imshow(image2)
subplot2.axis('off')
subplot2.set_title("Mean CO\N{SUBSCRIPT TWO} Emissions of Different Countries\n from 1997 to 2014", fontsize=8)

subplot3 = plt.subplot(grid[1, 1])
subplot3.imshow(image3)
subplot3.axis('off')
subplot3.set_title("Pie Chart of Different Types of \nElecricity Production in United States", fontsize=8)

subplot4 = plt.subplot(grid[2, 0])
subplot4.imshow(image4)
subplot4.axis('off')
subplot4.set_title("Heatmap Comparing Different Kinds of \nElectricity Production in United States", fontsize=8)

fig.suptitle("Impact of Different Kinds Electricity Production \non CO2 Emissions", fontsize=16)

plt.tight_layout()
plt.show()



                 