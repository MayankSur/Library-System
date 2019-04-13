
#This shall be run to set up the environment
# Assumed that docker is installed

#Run the docker build

docker build -t flaskapp .

#Run the container with given name

docker run -d --name libraryapp --publish 5000:4000 flaskapp

#The system should be up and running and accessible on port 5000 of host machine
echo "Application is up and running"
