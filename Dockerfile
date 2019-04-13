#First DockerFile
FROM ubuntu:16.04

MAINTAINER Your Name "mayank.surana@oliverwyman.com"

#Install Python and pip
#-y acts as a confirmation
RUN apt-get update
RUN apt-get install -y python python-pip

# We copy everything over
COPY . /app

#Creates a new working directory
WORKDIR /app

#Install the requirements
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
