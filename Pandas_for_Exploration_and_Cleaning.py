#Import the pandas library
import pandas as pd 

#Extract the new CSV Data:
df = pd.read_csv('sales_data_new.csv')

#Show info of the data:
print(df.info())

#Count the null values
print(df.isnull().sum())

#Remove the Irrlevant Column
df = df.drop('irrelevant_column_1', axis=1)

#Count the null values
print(df.isnull().sum())

#Update the Date
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#Aggregate the DataFrame
sales_by_product = df.groupby('product')['sales'].sum()
print(sales_by_product)

#Create Profit Column
#Debug and eradicate any strings or excessive floats:
df = df.dropna()
df['price'] = [ int(float(x))for x in df['price']]
df['cost'] = [ int(float(x))for x in df['cost']]

#Create the profit column now:
df['profit'] = df['price'] - df['cost']
print(df.head())

#Get intelligence on the data:
print(df['profit'].mean())
print(df['profit'].median())
print(df.describe())