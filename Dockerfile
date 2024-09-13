# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /football_prediction

# Install Airflow
RUN pip install apache-airflow==2.10.1

# Copy the Python script to the container
COPY test.py .

# Environment variables for Airflow
ENV AIRFLOW_HOME=/football_prediction/airflow_home

# Initialize Airflow database
RUN airflow db init

# Run the Python script
CMD ["airflow", "webserver"]
