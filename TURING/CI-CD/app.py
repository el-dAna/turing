import pandas as pd
import numpy as np
import argparse
from io import StringIO


def clean_data(data_file, cleaned_data_file="cleaned_data.csv"):
    """
    Cleans the input CSV data by handling missing values, removing duplicates,
    and encoding categorical variables.
    The cleaned data is saved to a specified CSV file.

    Parameters:
    ----------
    data_file : str
        Path to the input data file (CSV) that needs to be cleaned.

    cleaned_data_file : str, optional
        Path to save the cleaned data file (CSV).
        Defaults to 'cleaned_data.csv'.

    Returns:
    -------
    None
        This function does not return a value.
        It prints the original and cleaned DataFrames
        and saves the cleaned DataFrame to a CSV file.
    """

    # Read the CSV data into a DataFrame
    df = pd.read_csv(data_file)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Step 1: Remove unnecessary columns (if any)
    df.drop(
        columns=["ID"], inplace=True
    )  # Dropping ID as it's not useful for ML

    # Step 2: Handle missing values and replace 'NAN' string with actual np.nan
    df.replace("NAN", np.nan, inplace=True)

    # Convert Salary to numeric and coerce errors (this will convert
    # non-numeric entries to NaN)
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    # Fill numerical columns with the mean where appropriate
    df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill
