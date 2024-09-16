FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt .
# Copy the rest of the application code into the container
COPY . /code/

# Install the dependencies
RUN python -m venv /env
RUN chmod +x -R /env
RUN /env/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



# Copy the entrypoint file into the container
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Set the environment variable for Django
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRTEBYTECODE 1
