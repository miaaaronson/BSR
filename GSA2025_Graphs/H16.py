import pandas as pd
import matplotlib.pyplot as plt

# importing raw data (like from a raw CSV or excel file that someone downloaded and gave to me)
raw_df_16 = pd.read_csv("/Users/miaaaronson/Desktop/BSR/Data/H16_GSA.csv")

df_16 = raw_df_16[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

df_16["Date-Time (EST/EDT)"] = pd.to_datetime(df_16["Date-Time (EST/EDT)"])
plt.plot(df_16["Date-Time (EST/EDT)"], df_16["Date-Time (EST/EDT)"])

# assinging x and y variables
x16 = df_16["Date-Time (EST/EDT)"]
y16 = df_16["Temperature , °C"]

# identifying max and mins in df
max_temp = df_16.loc[df_16["Temperature , °C"].idxmax()]
min_temp = df_16.loc[df_16["Temperature , °C"].idxmin()]

raw_df_1 = pd.read_excel(
    "/Users/miaaaronson/Desktop/BSR/Data/BSR-H1 2025-03-19 12_50_32 EDT (Data EDT).xlsx"
)

df_1 = raw_df_1[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

df_1["Date-Time (EST/EDT)"] = pd.to_datetime(df_1["Date-Time (EST/EDT)"])
plt.plot(df_1["Date-Time (EST/EDT)"], df_1["Date-Time (EST/EDT)"])

# assinging x and y variables
x1 = df_1["Date-Time (EST/EDT)"]
y1 = df_1["Temperature , °C"]

# smoothed y values
y16_smooth = y16.rolling(window=300, center=True).mean()
y1_smooth = y1.rolling(window=300, center=True).mean()

# general plot features
plt.figure(figsize=(12, 6))
plt.plot(x1, y1_smooth, label="H1", color="#BCD2E8")
plt.plot(x16, y16_smooth, label="H16", color="#0818A8")
plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.legend()
plt.title("BSR HOBO-16 092024-022025")


plt.show()
