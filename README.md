# Notes App

This project is a lightweight note management app that allows users to create and list notes. It leverages Django Rest Framework for the backend and Vanilla JavaScript to interact with the GET endpoint.

<img src="https://github.com/user-attachments/assets/1e4b70f7-3e45-42f3-a491-3c6d268a0074"
     alt="project example"
     style="width:70%; border-radius: 8px;" />

# Installation

Requirements:
- Docker
- Docker compose

In this project we're using docker and docker-compose to facilitate the installation and replication of the development environment, define volumes and custom networks.

`docker-compose build`

Run project:

`docker-compose up`

In this case, we are using requirements.txt to install dependencies, but in the future we could implement poetry to manage dependencies in Docker.

Shut down the project:

`docker-compose down`
