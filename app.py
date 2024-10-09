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
# Fill numerical columns with the mean or median
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill NaN in Age with mean
# df['Salary'].fillna(df['Salary'].mean(), inplace=True)  # Fill NaN in Salary with mean
df['Department'].fillna('Department', inplace=True)  # Fill NaN in Department with a placeholder

# Step 3: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 4: Encode categorical variables
# Using OneHotEncoder for categorical columns like Department and Name
categorical_features = ['Name', 'Department']
numerical_features = ['Age', 'Salary']

# Create a column transformer to apply transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),   # Scale numerical features
        ('cat', OneHotEncoder(drop='first'), categorical_features)  # One-hot encode categorical features
    ])

# Step 5: Create a pipeline for preprocessing
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Step 6: Fit and transform the data using the pipeline
cleaned_data = pipeline.fit_transform(df)

# Convert the cleaned data back to a DataFrame for easier interpretation (optional)
cleaned_df = pd.DataFrame(cleaned_data)

# Display the cleaned DataFrame
print("\nCleaned DataFrame ready for Machine Learning:")
print(cleaned_df)