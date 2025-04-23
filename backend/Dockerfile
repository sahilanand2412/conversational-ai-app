# Use Python 3.11 as base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy backend folder content into container
COPY ./backend /app/backend
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
