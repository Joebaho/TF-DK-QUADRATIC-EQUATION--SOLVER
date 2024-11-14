# Define Docker image resource and configure it to push to Docker Hub
resource "docker_image" "quadratic_solver_image" {
  name = "${var.dockerhub_username}/quadratic_solver_image:latest"
  
  build {
    context = "."
    tag     = ["${var.dockerhub_username}/quadratic_solver_image:latest"]
    build_arg = {
      foo = "quadratic_solver_image"
    }
    label = {
      author = "quadratic_solver_image"
    }
  }
}
# Define Docker container resource
resource "docker_container" "quadratic_solver_container" {
  name  = "quadratic_solver_app"
  image = docker_image.quadratic_solver_image.image_id
  
  ports {
    internal = 5000
    external = 5000
  }
  # Provisioner to set Docker restart policy to always
  provisioner "local-exec" {
    command = "docker update --restart always ${self.name}"
  }
}





