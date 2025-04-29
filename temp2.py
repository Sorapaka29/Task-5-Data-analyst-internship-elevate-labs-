import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset (replace 'titanic.csv' with your dataset file if needed)
df = pd.read_csv('titanic.csv')

# Save Histogram for Age
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('histogram_age.png')  # Save as PNG file
plt.close()  # Close the plot to avoid overlap

# Save Histogram for Fare
plt.figure(figsize=(8, 6))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Distribution of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.savefig('histogram_fare.png')  # Save as PNG file
plt.close()

# Save Boxplot for Age (by Survival Status)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Age')
plt.savefig('boxplot_age_survival.png')  # Save as PNG file
plt.close()

# Save Boxplot for Fare (by Survival Status)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare Distribution by Survival Status')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Fare')
plt.savefig('boxplot_fare_survival.png')  # Save as PNG file
plt.close()

# Save Scatterplot for Age vs. Fare
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Fare', data=df, hue='Survived', palette='coolwarm', alpha=0.7)
plt.title('Age vs. Fare by Survival Status')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig('scatterplot_age_fare.png')  # Save as PNG file
plt.close()

# Save Pairplot for multiple variables (Age, Fare, Pclass, SibSp)
sns.pairplot(df[['Age', 'Fare', 'Pclass', 'SibSp', 'Survived']], hue='Survived', palette='coolwarm')
plt.suptitle('Pairwise Relationships by Survival Status', y=1.02)
plt.savefig('pairplot_relationships.png')  # Save as PNG file
plt.close()

# Save Heatmap for correlation between numeric columns
plt.figure(figsize=(10, 8))
corr_matrix = df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']].corr()  # Selecting numeric columns
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')  # Save as PNG file
plt.close()