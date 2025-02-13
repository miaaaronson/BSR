import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

# importing raw data (like from a raw CSV or excel file that someone downloaded and gave to me)
raw_df = pd.read_excel(
    "/Users/miaaaronson/Desktop/BSR/Data/FM-Temp-21852523-CT 2025-02-07 15_07_08 EST (Data EST).xlsx"
)

df = raw_df[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

df.head()

# assinging x and y variables
x = df["Date-Time (EST/EDT)"]
y = df["Temperature , °C"]

# identifying max and mins in df
max_temp = df.loc[df["Temperature , °C"].idxmax()]
min_temp = df.loc[df["Temperature , °C"].idxmin()]

# smoothed y values
y_smooth = signal.savgol_filter(y, window_length=500, polyorder=3, mode="nearest")

# general plot features
plt.plot(x, y, label="Raw Data", color="#BCD2E8")
plt.plot(x, y_smooth, label="Smoothed Data", color="#0818A8")
plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.legend()
plt.title("BSR HOBO-16 092024-022025")

# plotting the max and mins
plt.scatter(max_temp["Date-Time (EST/EDT)"], max_temp["Temperature , °C"], color="red")
plt.scatter(
    min_temp["Date-Time (EST/EDT)"], min_temp["Temperature , °C"], color="green"
)

# annotating the max and mins
plt.annotate(
    f"Max: {max_temp['Temperature , °C']:.2f}\n({max_temp['Date-Time (EST/EDT)'].date()})",
    (max_temp["Date-Time (EST/EDT)"], max_temp["Temperature , °C"]),
    textcoords="offset points",
    xytext=(15, -11),
    ha="left",
    color="red",
)

plt.annotate(
    f"Min: {min_temp['Temperature , °C']:.2f}\n({min_temp['Date-Time (EST/EDT)'].date()})",
    (min_temp["Date-Time (EST/EDT)"], min_temp["Temperature , °C"]),
    textcoords="offset points",
    xytext=(-5, 0),
    ha="right",
    color="green",
)

plt.show()
