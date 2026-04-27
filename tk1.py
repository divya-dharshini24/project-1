import pandas as pd
df=pd.read_csv(r"C:\Users\ADMIN\OneDrive\문서\internship\Task3\AB_NYC_2019.csv",encoding="latin1")
df.info()
df.describe()
df.isnull().sum()
df.fillna({
    "name":"Unknown",
    "host_name":"Unknown",
    "last_review":"No review",
    "reviews_per_month":0,
},inplace=True)
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df.drop_duplicates(inplace=True)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.title("Box plot")
plt.boxplot(df["price"])
plt.ylabel("Price")
plt.show()
numeric_cols = ['price','minimum_nights','number_of_reviews','reviews_per_month','latitude','longitude']
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"{col} outliers: {len(outliers)}")

plt.figure(figsize=(8,5))
plt.boxplot(df["minimum_nights"])
plt.xlabel("minimum_nights")
plt.title("Box plot for minimum nights")
plt.show()

plt.figure(figsize=(12,5))
plt.scatter(df["latitude"],df["longitude"],alpha=0.3)
plt.title("latitude vs Longitude")
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.show()
