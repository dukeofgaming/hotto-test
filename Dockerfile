# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables (optional, for Flask)
ENV FLASK_APP=hotto.app

# Default command to run the app
CMD ["python", "-m", "hotto.app"]
