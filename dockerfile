# Step 1: Start with a Python image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Copy the requirements file to the container
COPY requirements.txt /app/

# Step 5: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of the application into the container
COPY . /app/

# Step 7: Expose port 8000 for the app
EXPOSE 8000

# Step 8: Define the command to run the app using Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
