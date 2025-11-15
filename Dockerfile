FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application folder
COPY weather_app/ ./weather_app

# Expose Streamlit's default port
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "weather_app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
