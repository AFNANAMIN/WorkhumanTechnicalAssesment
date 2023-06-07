# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the ETL code to the working directory
COPY etl /app/etl

# Copy the main.py file to the working directory
COPY main.py /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app

# Create the 'data' directory
RUN mkdir data

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point command for the container
CMD ["python", "main.py"]