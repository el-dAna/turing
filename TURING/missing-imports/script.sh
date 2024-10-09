#!/bin/bash

# Define the paths for the data and the script
DATA_PATH="/workspaces/turing/TURING/missing-imports/data.csv"
SCRIPT_PATH="/workspaces/turing/app.py"
ARCHIVE_PATH="/workspaces/turing/TURING/missing-imports/archive"

# Run the Python script for data cleaning
python3 "$SCRIPT_PATH" "$DATA_PATH"

# Define the output file name with the current date for archiving
OUTPUT_FILE="cleaned_data_$(date +%F).csv"

# Move the cleaned data to the archive directory
mv /workspaces/turing/TURING/missing-imports/cleaned_data.csv "$ARCHIVE_PATH$OUTPUT_FILE"

echo "Data cleaning and archiving completed."