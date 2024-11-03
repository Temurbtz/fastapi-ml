# FastAPI Machine Learning Project

## Overview

This project is a FastAPI application designed for serving machine learning models. It provides a RESTful API that allows users to interact with the machine learning models such as: ner model for named entity relationship and text classification model for text classification.

## Features

- FastAPI for building the API
- Docker containerization
- Scalable deployment with Kubernetes
- Error tracking with Sentry

## Prerequisites

- Python 3.7+
- Docker
- Kubernetes (for deployment)
- Access to a Docker registry (e.g., Docker Hub)
- Sentry DSN (for error tracking)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Temurbtz/fastapi-ml
   cd fastapi-ml
   docker build -t <image_name>  .
   docker run -d --name <name_of_your_container> -p 8000:8000 <image_name> 

2. Open postman or curl and send post request to: http://0.0.0.0:8000/  with /ner for ner model   /classify for classification model
   ```json
    { "texts": [ "Arsenal has scored 7 goals", "Microbs grow very fast", "Number of people reading book has increased globally" ] } 
   
## Or you can do this:
  ```bash 
   docker pull temur2000/ml_text_projects:latest
   docker run -d --name <name_of_your_container> -p 8000:8000 temur2000/ml_text_projects 


## If you have cluster in cloud you can do this, on local machine cluster it will not work because I added loadbalancer, kind or minikube does
## support load balancer:
   ```bash
   kubectl apply -f k88-deployment.yaml
   

