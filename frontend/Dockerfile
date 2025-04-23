# Use official Python base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy frontend code and shared requirements
COPY ./frontend /app/frontend
COPY ../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio default port
EXPOSE 7860

# Run Gradio app
CMD ["python", "frontend/app.py"]
