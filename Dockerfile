# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /

# Install system dependencies needed by PyAudio
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-dev \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY demo_server.py .

# Run the server
CMD ["python", "demo_server.py"]
