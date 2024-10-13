import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


df = df = pd.read_csv("/workspaces/turing/TURING/missing-imports/data.csv")

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Step 1: Remove unnecessary columns (if any)
df.drop(columns=['ID'], inplace=True)  # Dropping ID as it's not useful for ML

# Step 2: Handle missing values
# Replace 'NAN' string with actual np.nan for proper handling of missing values
df.replace('NAN', np.nan, inplace=True)

# Fill numerical columns with the mean or median where appropriate
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill NaN in Age with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)  # Fill NaN in Salary with mean
df['Department'].fillna('Unknown', inplace=True)  # Fill NaN in Department with a placeholder

# Step 3: Remove duplicates based on Name and Age (you can adjust this based on your needs)
df.drop_duplicates(subset=['Name', 'Age'], inplace=True)

# Step 4: Encode categorical variables if needed (e.g., one-hot encoding)
df = pd.get_dummies(df, columns=['Department'], drop_first=True)


# Step 5: Save the cleaned DataFrame to a CSV file
df.to_csv('cleaned_data.csv', index=False)

print("\nCleaned data has been saved to 'cleaned_data.csv'.")