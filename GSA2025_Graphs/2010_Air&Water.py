import matplotlib.pyplot as plt
import pandas as pd


def MillersvilleAirTemp_FileConversion(html_path, csv_output, year="2010"):
    df_list = pd.read_html(html_path)
    df = df_list[0]

    if not all(col in df.columns for col in ["Date", "Time", "Temp. (oF)"]):
        raise ValueError("Missing required columns")

    df = df.iloc[1:]
    df = df.iloc[::-1].reset_index(drop=True)

    df["Temp. (oF)"] = (df["Temp. (oF)"] - 32) * 5 / 9

    df["Date"] = year + " " + df["Date"]

    df["Date and Time"] = pd.to_datetime(df["Date"] + " " + df["Time"], errors="coerce")

    final_df = df[["Date and Time", "Temp. (oF)"]]

    final_df.to_csv(csv_output, index=False)

    return final_df


# 07/15/2010
m_air_0715 = "/Users/miaaaronson/Desktop/BSR/Data/Hourly Observations at MU.html"
m_csv_air_0715 = "/Users/miaaaronson/Desktop/BSR/Data/Hourly Observations at MU.csv"
df_0715 = MillersvilleAirTemp_FileConversion(m_air_0715, m_csv_air_0715)

# 07/16/2010
m_air_0716 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07162010.html"
m_csv_air_0716 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07162010.csv"
df_0716 = MillersvilleAirTemp_FileConversion(m_air_0716, m_csv_air_0716)

# 07/17/2010
m_air_0717 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07172010.html"
m_csv_air_0717 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07172010.csv"
df_0717 = MillersvilleAirTemp_FileConversion(m_air_0717, m_csv_air_0717)

# 07/18/2010
m_air_0718 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07182010.html"
m_csv_air_0718 = "/Users/miaaaronson/Desktop/BSR/Data/m_air_07182010.csv"
df_0718 = MillersvilleAirTemp_FileConversion(m_air_0718, m_csv_air_0718)

all_air_df = pd.concat([df_0715, df_0716, df_0717, df_0718], ignore_index=True)
final_df = (
    all_air_df.set_index("Date and Time").resample("5T").interpolate()
)  # Adjust frequency as needed
final_df = all_air_df.reset_index()
print(all_air_df.head(50))

x = final_df[["Date and Time"]]
y = final_df[["Temp. (oF)"]]

plt.plot(x, y)
plt.xlabel("Date (XX-XX) and Time (-XX)")
plt.ylabel("Temperature in Degrees C")
plt.title("Air Temperature 2010 - Derived from Millersville University Archives")
plt.xticks(rotation=45)
plt.show()
