FROM python:3.8

# The enviroment variable ensures that the python output is set straight
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /starwars

# Set the working directory
WORKDIR /starwars

# Copy the current directory contents into the container
ADD . /starwars/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt