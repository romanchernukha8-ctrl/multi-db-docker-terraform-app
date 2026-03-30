terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_network" "app_network" {
  name = "app_network_v2"
}

resource "docker_container" "mysql" {
  name  = "mysql_dev"
  image = "mysql:8.0"

  networks_advanced {
    name = docker_network.app_network.name
  }

  env = [
    "MYSQL_ROOT_PASSWORD=root",
    "MYSQL_DATABASE=testdb",
    "MYSQL_USER=user",
    "MYSQL_PASSWORD=pass"
  ]

  ports {
    internal = 3306
    external = 3308
  }

  must_run = true
}

output "host" {
  value = "mysql_dev"
}

output "port" {
  value = 3306
}

output "user" {
  value = "user"
}

output "password" {
  value = "pass"
}

output "database" {
  value = "testdb"
}
