# Use a different base image, such as Python or any other necessary base
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install the weather-api dependencies here
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Add other configurations specific to the weather-api
