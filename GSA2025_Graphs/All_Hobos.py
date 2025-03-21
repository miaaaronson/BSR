import pandas as pd
import matplotlib.pyplot as plt

# H1
raw_df_1 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H1_GSA.xlsx")
df_1 = raw_df_1[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

# H2 MISSING

# H3
raw_df_3 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H3_GSA.xlsx")
df_3 = raw_df_3[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

# H4
raw_df_4 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H4_GSA.xlsx")
df_4 = raw_df_4[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H5
raw_df_5 = pd.read_excel(
    "/Users/miaaaronson/Desktop/BSR/Data/FM-Temp-21695006 2025-03-19 12_03_32 EDT (Data EDT).xlsx"
)
df_5 = raw_df_5[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H6 MISSING

# H7 MISSING

# H8 MISSING

# H9
raw_df_9 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H9_GSA.xlsx")
df_9 = raw_df_9[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H10 MISSING

# H11 DNE

# H12
raw_df_12 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H12_GSA.xlsx")
df_12 = raw_df_12[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H13
raw_df_13 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H13_GSA.xlsx")
df_13 = raw_df_13[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H14
raw_df_14 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H14_GSA.xlsx")
df_14 = raw_df_14[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]
# H15
raw_df_15 = pd.read_excel("/Users/miaaaronson/Desktop/BSR/Data/H15_GSA.xlsx")
df_15 = raw_df_15[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

# H16 (DNE)
raw_df_16 = pd.read_excel(
    "/Users/miaaaronson/Desktop/BSR/Data/BSR-H16 2025-03-21 10_16_29 EDT (Data EDT).xlsx"
)
df_16 = raw_df_16[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

# H23 (AIR TEMPERATURE AT MAIN BRANCH)
raw_df_23 = pd.read_excel(
    "/Users/miaaaronson/Desktop/BSR/Data/FM-Temp-21852523-CT 2025-03-19 10_47_18 EDT (Data EDT).xlsx"
)
df_23 = raw_df_23[
    [
        "Date-Time (EST/EDT)",
        "Temperature , °C",
    ]
]

df_1["Date-Time (EST/EDT)"] = pd.to_datetime(df_1["Date-Time (EST/EDT)"])
df_3["Date-Time (EST/EDT)"] = pd.to_datetime(df_3["Date-Time (EST/EDT)"])
df_4["Date-Time (EST/EDT)"] = pd.to_datetime(df_4["Date-Time (EST/EDT)"])
df_5["Date-Time (EST/EDT)"] = pd.to_datetime(df_5["Date-Time (EST/EDT)"])
df_9["Date-Time (EST/EDT)"] = pd.to_datetime(df_9["Date-Time (EST/EDT)"])
df_12["Date-Time (EST/EDT)"] = pd.to_datetime(df_12["Date-Time (EST/EDT)"])
df_13["Date-Time (EST/EDT)"] = pd.to_datetime(df_13["Date-Time (EST/EDT)"])
df_14["Date-Time (EST/EDT)"] = pd.to_datetime(df_14["Date-Time (EST/EDT)"])
df_15["Date-Time (EST/EDT)"] = pd.to_datetime(df_15["Date-Time (EST/EDT)"])
df_16["Date-Time (EST/EDT)"] = pd.to_datetime(df_16["Date-Time (EST/EDT)"])
df_23["Date-Time (EST/EDT)"] = pd.to_datetime(df_23["Date-Time (EST/EDT)"])


df_5 = df_5[df_5["Date-Time (EST/EDT)"] >= "2024-09-01"]

x1 = df_1["Date-Time (EST/EDT)"]
y1 = df_1["Temperature , °C"]

x3 = df_3["Date-Time (EST/EDT)"]
y3 = df_3["Temperature , °C"]

x4 = df_4["Date-Time (EST/EDT)"]
y4 = df_4["Temperature , °C"]

x5 = df_5["Date-Time (EST/EDT)"]
y5 = df_5["Temperature , °C"]

x9 = df_9["Date-Time (EST/EDT)"]
y9 = df_9["Temperature , °C"]

x12 = df_12["Date-Time (EST/EDT)"]
y12 = df_12["Temperature , °C"]

x13 = df_13["Date-Time (EST/EDT)"]
y13 = df_13["Temperature , °C"]

x14 = df_14["Date-Time (EST/EDT)"]
y14 = df_14["Temperature , °C"]

x15 = df_15["Date-Time (EST/EDT)"]
y15 = df_15["Temperature , °C"]

x16 = df_16["Date-Time (EST/EDT)"]
y16 = df_16["Temperature , °C"]

x23 = df_23["Date-Time (EST/EDT)"]
y23 = df_23["Temperature , °C"]

y1_smooth = y1.rolling(window=300, center=True).mean()
y3_smooth = y3.rolling(window=300, center=True).mean()
y4_smooth = y4.rolling(window=300, center=True).mean()
y5_smooth = y5.rolling(window=300, center=True).mean()
y9_smooth = y9.rolling(window=300, center=True).mean()
y12_smooth = y12.rolling(window=300, center=True).mean()
y13_smooth = y13.rolling(window=300, center=True).mean()
y14_smooth = y14.rolling(window=300, center=True).mean()
y15_smooth = y15.rolling(window=300, center=True).mean()
y16_smooth = y16.rolling(window=300, center=True).mean()
y23_smooth = y23.rolling(window=300, center=True).mean()

plt.figure(1, figsize=(10, 6))
plt.plot(x1, y1_smooth, label="H1", color="#f94144")
plt.plot(x3, y3_smooth, label="H3", color="#f3722c")
plt.plot(x4, y4_smooth, label="H4", color="#f8961e")
plt.plot(x5, y5_smooth, label="H5", color="#f9c74f")
plt.plot(x9, y9_smooth, label="H9", color="#90be6d")
plt.plot(x12, y12_smooth, label="H12", color="#43aa8b")
plt.plot(x13, y13_smooth, label="H13", color="#4d908e")
plt.plot(x14, y14_smooth, label="H14", color="#577590")
plt.plot(x15, y15_smooth, label="H14", color="#277da1")
plt.plot(x16, y16_smooth, label="H16", color="#6d597a")
plt.plot(x23, y23_smooth, label="H23 - Air Temperature", color="pink")
plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.legend()
plt.title("Fall - Early Spring HOBO Deployment at BSR")

plt.figure(2, figsize=(10, 6))
plt.plot(x1, y1_smooth, label="H1", color="#f94144")
plt.plot(x3, y3_smooth, label="H3", color="#f3722c")
plt.plot(x4, y4_smooth, label="H4", color="#f8961e")
plt.plot(x5, y5_smooth, label="H5", color="#f9c74f")
plt.plot(x9, y9_smooth, label="H9", color="#90be6d")
plt.plot(x12, y12_smooth, label="H12", color="#43aa8b")
plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.legend()
plt.title("Fall - Early Spring HOBO Deployment at BSR: Inside Restoration")

plt.figure(3, figsize=(10, 6))
plt.plot(x13, y13_smooth, label="H13", color="#4d908e")
plt.plot(x14, y14_smooth, label="H14", color="#577590")
plt.plot(x15, y15_smooth, label="H15", color="#277da1")
plt.plot(x16, y16_smooth, label="H16", color="#6d597a")
plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.legend()
plt.title("Fall - Early Spring HOBO Deployment at BSR: Above Restoration")

plt.show()
