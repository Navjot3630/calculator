# Use the official Python image from Docker Hub
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Specify the command to run your Flask app
CMD ["python", "app.py"]