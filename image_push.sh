#!/bin/bash
image_name="$dockerhub_username/quadratic_solver_image:latest"
export dockerhub_username="joebaho2"
export dockerhub_password="xxxxxxxxxxxxxxxxx"

# Login to Docker Hub
echo "Logging into Docker Hub..."
echo "$dockerhub_password" | docker login --username "$dockerhub_username" --password-stdin

# Push the image
echo "Pushing image $image_name to Docker Hub..."
docker push joebaho2/quadratic_solver_image:latest

echo "Image pushed successfully!"
