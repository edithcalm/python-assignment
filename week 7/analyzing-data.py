# load and explore datasets
import pandas as p
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the iris dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())


# Check structure, data types, and missing values
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

#  Task 2: Basic Data Analysis

print("\nBasic Statistics:")
print(df.describe())

# Group by 'target' (species) and calculate mean for each numeric column
df['species'] = df['target'].apply(lambda x: iris.target_names[x])
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# Observation Example
print("\nObservation: Setosa flowers tend to have smaller petal sizes than Versicolor and Virginica.")

# Task 3: Data Visualization
# 1. Line Chart - Mean petal length over index (not time-based, just for example)
plt.figure(figsize=(8, 4))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart of Petal Length")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(6, 4))
grouped["petal length (cm)"].plot(kind='bar', color='skyblue')
plt.title("Average Petal Length by Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# 3. Histogram - Distribution of sepal length
plt.figure(figsize=(6, 4))
plt.hist(df["sepal length (cm)"], bins=10, color='green', edgecolor='black')
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()
