# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /docker_football_test

# Copy the Python script to the container
COPY . .

# Install requirements
RUN pip install -r requirements.txt

RUN airflow db init

# Create an admin user
RUN airflow users create \
    --username admin \
    --password admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com

EXPOSE 8080

# Default commands
CMD ["airflow", "webserver", "--port", "8080"]