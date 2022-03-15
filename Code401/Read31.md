# Docker - Django REST

[wsvincent-docker](https://wsvincent.com/beginners-guide-to-docker/)

- Docker is a linux container.
- docker hub contains most common images
- image: a snapshot of an environment

## Docker Commands

- docker info
- docker image ls : inspect current image
- docker inspect image
- docker ps: list containers active
- docker ps -a : list all containers with history

- docker rmi image: remove image

- docker container ls -la: display all
- docker image build .  :builds from current Dockerfile

- Dockerfile: Image instructions
- docker-compose.yml: container instructions

### Dockerfile / Docker.yml

From: image

ENV: environment variable

WORKDIR: working directory

COPY: copy dependencies lock file
RUN: installation of dependencies

COPY . /code/   : copy project
