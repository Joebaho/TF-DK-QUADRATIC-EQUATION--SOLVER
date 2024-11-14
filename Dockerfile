# Dockerfile
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py /app
COPY . /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask
RUN pip install Flask

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Isntall Jinja2 
RUN pip install Jinja2==3.0.3
#upgrade Flask
RUN pip install --upgrade Flask

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
