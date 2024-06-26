# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD ./src /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches (use CMD instead if you want to pass 
CMD ["python", "app.py"]

