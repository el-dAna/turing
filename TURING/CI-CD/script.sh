#!/bin/bash

# Define the paths for the data and the script
DATA_PATH = "/workspaces/turing/TURING/CI-CD/data.csv"
SCRIPT_PATH = "/workspaces/turing/TURING/CI-CD/app.py"
ARCHIVE_PATH = "/workspaces/turing/TURING/CI-CD/archive"
CLEANED_DATA_PATH = "/workspaces/turing/TURING/CI-CD/cleaned_data.csv"

# Run the Python script for data cleaning
python3 "$SCRIPT_PATH" "$DATA_PATH" "$CLEANED_DATA_PATH"

# Define the output file name with the current date for archiving
OUTPUT_FILE = "cleaned_data_$(date +%F).csv"

# Move the cleaned data to the archive directory
mv "$CLEANED_DATA_PATH" "$ARCHIVE_PATH$OUTPUT_FILE"

echo "Data cleaning and archiving completed."
