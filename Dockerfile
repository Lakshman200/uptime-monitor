# Use official Python image as base
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask requests

# Expose port 5050
EXPOSE 5050

# Run the app
CMD ["python", "-m", "uptime_monitor.app"]

