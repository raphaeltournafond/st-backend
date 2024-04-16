# Use the official Python image from Docker Hub
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/