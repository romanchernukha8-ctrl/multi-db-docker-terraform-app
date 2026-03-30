terraform {
  required_version = ">= 1.0"
}

# Создание контейнера
resource "null_resource" "mysql_container" {
  provisioner "local-exec" {
    command = <<EOT
podman run -d \
  --name my-mysql \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=testdb \
  -p 3309:3306 \
  docker.io/library/mysql:8 || true
EOT
  }
}

# Удаление контейнера при destroy
resource "null_resource" "mysql_cleanup" {
  triggers = {
    container_id = null_resource.mysql_container.id
  }

  provisioner "local-exec" {
    when    = destroy
    command = "podman rm -f my-mysql || true"
  }
}
