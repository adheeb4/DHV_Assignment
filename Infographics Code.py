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
    """Function to read data drom csv file and transpose the data"""
    data = pd.read_csv(filename, skipfooter=5, engine='python')
    data_transposed = data.set_index("Country Name").transpose()
    data_transposed = data_transposed.drop(index=["Series Name"])
    return data_transposed


# List of countries to analyze
Countries_list = ["United Kingdom", "China", "United States",
                  "India", "Thailand", "Bangladesh"]


# Function to calculate the mean of a specific country's data
def mean(data_frame, country):
    mean = np.mean(data_frame[country])

    return mean


# Function to calculate the median of a specific country's data
def median(data_frame, country):
    median = np.median(data_frame[country[i]])

    return median


# Read and process the CO2 emission data
co2_emission = read_data('CO2 emissions (metric tons per capita).csv')
co2_emission = co2_emission[:18]
co2_emission = co2_emission.apply(pd.to_numeric)

# Read and process the electricity production from hydroelectric sources data
electricity_hydro = read_data('electricity_production_hydro.csv')
electricity_hydro = electricity_hydro[:18]
electricity_hydro = electricity_hydro.apply(pd.to_numeric)

# Read and process the electricity production from non-renewable sources data
electricity_nonrenewable = read_data('electricity_production_nonrenewable.csv')
electricity_nonrenewable = electricity_nonrenewable[:18]
electricity_nonrenewable = electricity_nonrenewable.apply(pd.to_numeric)

# Read and process the electricity production from nuclear sources data
electricity_nuclear = read_data('electricity_production_nuclear.csv')
electricity_nuclear = electricity_nuclear[:18]
electricity_nuclear = electricity_nuclear.apply(pd.to_numeric)

# Read and process the electricity production from renewable sources data
electricity_renewable = read_data('electricity_production_renewable.csv')
electricity_renewable = electricity_renewable[:18]
electricity_renewable = electricity_renewable.apply(pd.to_numeric)


# Create a figure with subplots
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(30, 16))
plt.subplots_adjust(hspace=0.3)

# Plot CO2 emissions for each country
for i in range(len(Countries_list)):
    ax[0, 0].plot(co2_emission.index, co2_emission[Countries_list[i]])
    ax[0, 0].set_title("CO\N{SUBSCRIPT TWO} emissions (metric tons per capita)", size=20)
    ax[0, 0].set_xticklabels(co2_emission.index, rotation=90)
    ax[0, 0].grid(True)
    ax[0, 0].set_xlabel("Year", size=16)
    ax[0, 0].set_ylabel("CO\N{SUBSCRIPT TWO} Emission\n (metric tons per capita)", size=16)

# Plot electricity production from hydroelectric sources for each country
for i in range(len(Countries_list)):
    ax[0, 1].plot(electricity_hydro.index, electricity_hydro[Countries_list[i]])
    ax[0, 1].set_title("Electricity production from \nhydroelectric sources (% of total)", size=20)
    ax[0, 1].set_xticklabels(electricity_hydro.index, rotation=90)
    ax[0, 1].grid(True)
    ax[0, 1].set_xlabel("Year", size=16)
    ax[0, 1].set_ylabel("Electricity production from \nhydroelectric sources (% of total)", size=16)

# Plot electricity production from non-renewable sources for each country
for i in range(len(Countries_list)):
    ax[0, 2].plot(electricity_nonrenewable.index, electricity_nonrenewable[Countries_list[i]])
    ax[0, 2].set_title("Electricity production from\n oil, gas and coal sources (% of total)", size=20)
    ax[0, 2].set_xticklabels(electricity_nonrenewable.index, rotation=90)
    ax[0, 2].grid(True)
    ax[0, 2].set_xlabel("Year", size=16)
    ax[0, 2].set_ylabel("Electricity production from \noil, gas and coal sources (% of total)", size=16)


# Plot electricity production from nuclear sources for each country
for i in range(len(Countries_list)):
    ax[1, 0].plot(electricity_nuclear.index, electricity_nuclear[Countries_list[i]])
    ax[1, 0].set_title("Electricity production from\n nuclear sources (% of total)", size=20)
    ax[1, 0].set_xticklabels(electricity_nuclear.index, rotation=90)
    ax[1, 0].grid(True)
    ax[1, 0].set_xlabel("Year", size=16)
    ax[1, 0].set_ylabel("Electricity production from\n nuclear sources (% of total)", size=16)

# Plot electricity production from renewable sources for each country
for i in range(len(Countries_list)):
    ax[1, 1].plot(electricity_renewable.index, electricity_renewable[Countries_list[i]])
    ax[1, 1].set_title("Electricity production from renewable sources,\n excluding hydroelectric (% of total)", size=20)
    ax[1, 1].set_xticklabels(electricity_renewable.index, rotation=90)
    ax[1, 1].grid(True)
    ax[1, 1].set_xlabel("Year", size=16)
    ax[1, 1].set_ylabel("Electricity production from renewable sources,\n excluding hydroelectric (% of total)", size=16)

# Remove the last subplot
ax[1, 2].remove()

# Add a legend to the plot
ax_legend = fig.add_subplot(2, 2, 4)
ax[0, 0].legend(Countries_list, fontsize=23, bbox_to_anchor=(3.17, -0.4))
ax_legend.axis('off')

# Save the figure as image1.png
plt.savefig("image1.png", dpi=300, bbox_inches="tight")

plt.figure()

# Plot the mean CO2 emissions for each country
mean_co2_list = [np.mean(co2_emission["United Kingdom"]),
                 np.mean(co2_emission["China"]),
                 np.mean(co2_emission["United States"]),
                 np.mean(co2_emission["India"]),
                 np.mean(co2_emission["Thailand"]),
                 np.mean(co2_emission["Bangladesh"])]

plt.barh(Countries_list, mean_co2_list)
plt.ylabel("Countries")
plt.xlabel("CO\N{SUBSCRIPT TWO} Emission(metric tons per capita)")
plt.savefig("image2.png", dpi=300, bbox_inches="tight")


mean_data_us = [np.mean(electricity_hydro["United States"]),
                np.mean(electricity_nonrenewable["United States"]),
                np.mean(electricity_nuclear["United States"]),
                np.mean(electricity_renewable["United States"])]
plt.figure()

# Plot a pie chart of different types of electricity production in the United States
plt.pie(mean_data_us, autopct="%1.1f%%")
plt.legend(bbox_to_anchor=(1, 1),
           labels=["Hydroelectric sources",
                   "Oil, gas and coal sources",
                   "Nuclear sources",
                   "Renewable sources, \nexcluding hydroelectric"])
plt.savefig("image3.png", dpi=300, bbox_inches="tight")

# Create a DataFrame for the United States data
dfi_us = pd.DataFrame(co2_emission.index)
df1_us = pd.DataFrame(co2_emission["United States"]).rename(columns={"United States": "CO2 Emission"})
df2_us = pd.DataFrame(electricity_hydro["United States"]).rename(columns={"United States": "Electricity Production(Hydro)"})
df3_us = pd.DataFrame(electricity_nonrenewable["United States"]).rename(columns={"United States": "Electricity Production(Non Renewable)"})
df4_us = pd.DataFrame(electricity_nuclear["United States"]).rename(columns={"United States": "Electricity Production(Nuclear)"})
df5_us = pd.DataFrame(electricity_renewable["United States"]).rename(columns={"United States": "Electricity Production(Renewable)"})

data_us = pd.concat([dfi_us, df1_us, df2_us, df3_us, df4_us, df5_us], axis=1)
data_us.drop(data_us.index[:18], inplace=True)
data_us.drop(data_us.columns[0], axis=1, inplace=True)

plt.figure()

# Plot a heatmap of the correlation between different types of electricity production in the United States
corr = data_us.corr()
sns.heatmap(corr, annot=True, linewidths=0, square=True, cmap='Blues')
plt.savefig("image4.png", dpi=300, bbox_inches="tight")

# Create infographics dashboard using plots with gridspec
fig = plt.figure(figsize=(6, 10))
grid = gridspec.GridSpec(3, 2, figure=fig, wspace=0.1, hspace=0.1)

image1 = imread('image1.png')
image2 = imread('image2.png')
image3 = imread('image3.png')
image4 = imread('image4.png')
image5 = imread('image5.png')

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

subplot5 = plt.subplot(grid[2, 1])
subplot5.axis('off')
subplot5.imshow(image5)

fig.suptitle("Impact of Different Kinds Electricity Production\non CO2 Emissions", fontsize=16, weight="bold")
plt.tight_layout()

# Save Infographics Dashboard as png
plt.savefig("21085206.png", dpi=300, bbox_inches="tight")
plt.show()         