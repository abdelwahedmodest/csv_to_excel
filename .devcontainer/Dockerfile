# Use an official Python runtime as a parent image
FROM python:3.9.0

# Set the working directory in the container
WORKDIR /c/Users/lenovo/Desktop/Waiting/Septembre/06092024/1

# Copy the requirements file into the container at /usr/src/app/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app/
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Définir la commande de démarrage
CMD ["python", "main.py"]
