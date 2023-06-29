# Common Questions
## Why not just use VM's?
- Runs on containers which are run on the host's OS, unlike VM's which replicate an OS

## Packages applications with all their dependencies into one unit
- Significantly faster than VM's, low overhead
- Decouples a user's OS with an application

## What is BusyBox?
- Packages multiple unix commands in one container

## How do Containers work?
- A new container is created every time you run an image

## What are Images?
- Blueprints for containers

## What is the Docker Daemon?
- Background service that manages Docker Containers

## What is a Docker Client?
- Basically CLI

## What is Docker Hub?
- Basically GitHub but for Docker

## What are Tags?
- Specify a version of the image, similar to their common use-case in Git

## What are Base Images vs Child Images and Official Images vs User Images
- Base Images have no depedencies (OS's)
- Child Images build off Base Images
- Official Images are maintained by the Docker staff
- User Images are made by the people, typically formatted as ```user/image-name```
- All User Images are based on Base Images

## What is a Dockerfile
- An init file when creating an image

# Common Commands
## How to Install Images
- __COMMAND__ -> docker pull image-name
- By default pulls from [Docker Hub](https://hub.docker.com/search?q=)
### Common Options
- __COMMAND__ -> docker pull image-name:tag

## How to Find Images?
- __COMMAND__ -> docker search image-name
- [Docker Hub](https://hub.docker.com/search?q=)

## How to run a Docker Image
- __COMMAND__ -> docker run image-name
### Common Options
- -it -> Attach a new command-line
- --rm -> Deletes container on exit
- -d -> Detach terminal from shell
- --name -> Specify container name

### Networking Options
- -P -> Set the container on a random port
- -p -> server-port:exposed-port

## How to list all Docker Containers?
- __COMMAND__ -> docker ps (only shows running containers)
- __COMMAND__ -> docker ps -a (includes past containers)

## How to list all Dockert Images?
- __COMMAND__ -> docker images

## How to delete a Container?
- __COMMAND__ -> docker rm container-id
- __COMMAND__ -> docker rm $(docker ps -a -q -f status=exited) (deletes all exited containers)
- __COMMAND__ -> docker container prune / dockerclean (alias for docker rm $(docker ps -a -q -f status='exited') -> Both commands delete all exited containers
- __COMMAND__ -> docker stop container-id

## How to delete an Image?
- __COMMAND__ -> docker rmi image-name

# Networking Commands
## How to view what port your container is on?
- __COMMAND__ -> docker port container-name

## How to create an Image?
- __COMMAND__ -> docker build path

### Common Options
- -t -> username/image-name (on Dockerhub)

## Docker Hub
### How to upload your Image to Docker Hub?
- __COMMAND__ -> docker push username/image-name

### How to login to Docker Hub?
- __COMMAND__ -> docker login

# Dockerfile Syntax
## Specify Base Images used
- FROM base-image:tag

## How to specify where the Image will be installed?
- WORKDIR /path

## How to copy files to Image directory?
- COPY . .

## How to run a specific command on Container start-up?
- CMD ["command", "command-arg1"]

# Docker with AWS
## What is Dockerrun.aws.json?
- AWS specific init file for a Beanstalk environment
