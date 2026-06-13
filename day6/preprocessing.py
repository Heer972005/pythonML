'''
This dataset contains 55,000 synthetic customer transactions generated using Python's Faker library.
It simulates real-world retail transactions and can be used for data preprocessing, statistical analysis, 
and visualization.

Shape of Dataset
Rows: 55,000
Columns: 13


| Column                | Description                        |
| --------------------- | ---------------------------------- |
| CID                   | Unique Customer ID                 |
| TID                   | Unique Transaction ID              |
| Gender                | Male, Female, Other                |
| Age Group             | Customer age category              |
| Purchase Date         | Date and time of transaction       |
| Product Category      | Category of purchased product      |
| Discount Availed      | Whether discount was used (Yes/No) |
| Discount Name         | Name of discount applied           |
| Discount Amount (INR) | Amount of discount received        |
| Gross Amount          | Amount before discount             |
| Net Amount            | Final amount after discount        |
| Purchase Method       | Credit Card, Debit Card, UPI, etc. |
| Location              | City where purchase occurred       |
import kagglehub

# Download latest version
path = kagglehub.dataset_download("shrishtimanja/ecommerce-dataset-for-data-analysis")

print("Path to dataset files:", path)
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("project1_df.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.head())

df["Purchase Date"] = pd.to_datetime(
    df["Purchase Date"],
    format="%d/%m/%Y %H:%M:%S"
)
df["Year"] = df["Purchase Date"].dt.year
df["Month"] = df["Purchase Date"].dt.month
df["Day"] = df["Purchase Date"].dt.day
print(df["Purchase Date"].dtypes)

print(df.isnull().sum())
print((df.isnull().sum()/len(df))*100)
df["Discount Name"] = df["Discount Name"].fillna("No Discount")

print(df.duplicated().sum())

#statistics
print(df.describe())
print("Mean Gross Amount =", df["Gross Amount"].mean())
print("Mean Net Amount =", df["Net Amount"].mean())
print("Mean Discount Amount =", df["Discount Amount (INR)"].mean())
print("Median of Gross Amount",df["Gross Amount"].median())
print("Median of Net Amount",df["Net Amount"].median())
print("Std of Gross Amount",df["Gross Amount"].std())
print("Std of Net Amount",df["Net Amount"].std())
print("Minimum of Gross Amount",df["Gross Amount"].min())
print("Maximum of Gross amount",df["Gross Amount"].max())

print(df[["Gross Amount", "Discount Amount (INR)", "Net Amount"]].corr())

print(df["Gender"].value_counts())
print("\n",df["Purchase Method"].value_counts())
print("\n",df["Location"].value_counts())

#plotting

plt.figure(figsize=(8,5))
plt.hist(df["Net Amount"], bins=20, color="#a3b5c7", edgecolor="black")
plt.xlabel("Net Amount")
plt.ylabel("Frequency")
plt.title("Distribution of Net Amount")
plt.show()

df.loc[0, "Gross Amount"] = 10000
plt.figure(figsize=(8,5))
plt.boxplot(df["Gross Amount"],
            patch_artist=True,
            boxprops=dict(facecolor='skyblue', color='black'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='black'),
            capprops=dict(color='purple'),
            flierprops=dict(marker='*',
                    markerfacecolor='orange',
                    markersize=8,
                    markeredgecolor='red'))
plt.title("Boxplot of Gross Amount")
plt.show()
Q1 = df["Gross Amount"].quantile(0.25)
Q2 = df["Gross Amount"].quantile(0.50)
Q3 = df["Gross Amount"].quantile(0.75)
IQR = Q3 - Q1
print("Lower limit =", Q1 - 1.5*IQR)
print("Upper limit =", Q3 + 1.5*IQR)
print("Q1 =", Q1)
print("Median =", Q2)
print("Q3 =", Q3)

df["Product Category"].value_counts().plot(kind='bar')
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.title("Product Category Distribution")
plt.xticks(rotation=45)
plt.show()

df["Purchase Method"].value_counts().plot(kind='bar')
plt.xlabel("Purchase Method")
plt.ylabel("Count")
plt.title("Purchase Method Distribution")
plt.show()

df["Gender"].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.ylabel("")
plt.title("Gender Distribution")
plt.show()

df["Location"].value_counts().head(10).plot(kind='bar')
plt.xlabel("City")
plt.ylabel("Number of Purchases")
plt.title("Top 10 Locations")
plt.xticks(rotation=45)
plt.show()