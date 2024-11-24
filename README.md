[![Build and Push Docker Image](https://github.com/nogibjj/Mobasserul_Haque_MiniProject12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mobasserul_Haque_MiniProject12/actions/workflows/cicd.yml)

# Dockerized Application

## Project Overview

This project demonstrates a simple Python Flask application containerized using Docker. The application calculates the user's age based on their Date of Birth (DOB). The project incorporates CI/CD to automate building and pushing the Docker image to Docker Hub.

---
## Features

- **Flask Web Application**: A web application that calculates age from the provided Date of Birth.
- **Dockerized Deployment**: The application is containerized for seamless deployment across environments.
- **Makefile Automation**: Simplifies Docker commands for building, running, and pushing the container.
- **CI/CD Integration**: Automates the Docker build and push process using GitHub Actions.

---

## Directory Structure

```
├── .github/
│   └── workflows/
│       └── cicd.yml
├── .coverage
├── .gitignore
├── app.py
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt

```
## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/nogibjj/Mobasserul_Haque_MiniProject12.git
cd Mobasserul_Haque_MiniProject12
```

2. **Build the Docker Image**

Build the Docker image using the Makefile:

```bash
make build
```

3. **Run the Docker Container**

```bash
make run
```
Access the application in your browser at [http://localhost:5000](http://localhost:5000).

4. **Push the Docker Image to Docker Hub**

Authenticate with Docker Hub and push the image:

```bash
make push
```
## Flask Application Details

### Endpoints

- **Home Page (`/`)**: Displays a form for users to enter their Date of Birth.
![app_img1](app_img1.PNG)

- **Calculate Age (`/calculate_age`)**: Processes the DOB input and calculates the user's age.
![app_img2](app_img2.PNG)
---
## CI/CD Integration

This project uses GitHub Actions to automate Docker image builds and deployments. The workflow (`.github/workflows/cicd.yml`) performs the following steps:

1. **Checks out the repository**
2. **Logs into Docker Hub** using repository secrets
3. **Builds the Docker image**
4. **Pushes the image to Docker Hub**

## Deployment to Docker Hub

### Manually

1. **Log in to Docker Hub:**

```bash
	docker login -u ${DOCKER_ID_USER}
```
![DockerHub_Repo_Img1](DockerHub_Repo_Img1.PNG)

2. **Tag the Docker Image:**

```bash
docker tag dockerized_app <your-dockerhub-username>/dockerized_app:latest
```

3. **Push the Image:**

```bash
docker push mobasserulhaque/mh_de_week12:tagname
```
4. **Pull the Image:**

```bash
docker pull mobasserulhaque/mh_de_week12:latest
```
![DockerHub_Repo_Img2](DockerHub_Repo_Img2.PNG)
![DockerHub_Repo_Img3](DockerHub_Repo_Img3.PNG)

### Using Make Commands

Alternatively, use the following command to simplify the process:

```bash
make push
```

---

## Docker Hub Details

- **Docker Image:** [dockerized_app_image_Link](https://hub.docker.com/repository/docker/mobasserulhaque/mh_de_week12)
- **Tag:** `latest`

---