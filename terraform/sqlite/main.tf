terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

provider "local" {}

resource "local_file" "db_file" {
  filename = abspath("${path.module}/database.db")
  content  = ""
}

output "db_path" {
  value = local_file.db_file.filename
}
