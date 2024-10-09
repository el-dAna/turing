# Use an existing Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file into the container
COPY requirements.txt .

# Install dependencies in the container
RUN pip install -r requirements.txt

# Copy the Python file into the container
COPY app.py .

# Run the Python file when the container starts
CMD ["python", "app.py"]