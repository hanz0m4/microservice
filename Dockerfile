# Use the official Python image
FROM python:3.10-alpine


# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local app directory to the working directory
COPY . .

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--port", "8000"]