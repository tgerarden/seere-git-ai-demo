import pandas as pd

df = pd.read_csv("data/analysis_data.csv")

# Basic overview
print(df.shape)
print(df.head())

# Mean CO2 per capita by country (full sample)
co2_by_country = (
    df.groupby("country")["CO2_transport_capita"]
    .mean()
    .sort_values(ascending=False)
)
print(co2_by_country)

co2_by_country.to_csv("output/tables/co2_by_country.csv") 