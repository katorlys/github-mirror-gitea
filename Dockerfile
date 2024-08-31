FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy contents in current directory into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the script container launches
ENTRYPOINT ["python", "main.py"]