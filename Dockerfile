# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in a requirements.txt file
# If you have a requirements.txt, use this:
RUN pip install --no-cache-dir -r requirements.txt

# If you don't have a requirements.txt and want to install specific packages, use this:
# Example: RUN pip install --no-cache-dir fastapi uvicorn
#      Replace 'fastapi uvicorn' with your actual dependencies.

# Expose the port that your FastAPI application will run on
#  The default FastAPI port is 8000.  Change if needed.
EXPOSE 8000

# Specify the command to run your application using Uvicorn
#  --host 0.0.0.0 makes the app accessible from outside the container
#  --port 8000  sets the port
#  --reload enables hot reloading (for development).  Remove in production.
#  "main:app" refers to the main.py file and the 'app' FastAPI instance within it.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
