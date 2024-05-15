# FROM python:3 

# RUN pip install virtualenv
# ENV VIRTUAL_ENV=/venv
# RUN virtualenv venv -p python3
# ENV PATH="VIRTUAL_ENV/bin:$PATH"
# RUN pip install gunicorn

# WORKDIR /app
# ADD . /app

# # Install dependencies
# RUN pip install -r requirements.txt

# # Expose port 
# ENV PORT 8080

# # Run the application:
# CMD ["gunicorn", "app:app"]

FROM python:3.7

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install virtualenv globally
RUN pip install virtualenv

# Set up a virtual environment
RUN virtualenv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install gunicorn in the virtual environment
RUN pip install gunicorn

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
ENV PORT 8080

# Run the application:
CMD ["gunicorn", "app:app"]
