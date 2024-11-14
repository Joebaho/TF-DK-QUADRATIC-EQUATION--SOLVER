terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  # Using environment variables to set Docker Hub credentials
  registry_auth {
    address  = "https://index.docker.io/v1/"
    username = var.dockerhub_username  # or directly "your_dockerhub_username"
    password = var.dockerhub_password  # or directly "your_dockerhub_password"
  }
}