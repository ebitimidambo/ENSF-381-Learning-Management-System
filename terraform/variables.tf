variable "instance_name" {
  description = "Name of the EC2 instance deployed by Terraform."
  type        = string
  default     = "ENSF519-Final-Project-Server"
}

variable "instance_type" {
  description = "EC2 instance type for the application server."
  type        = string
  default     = "t3.small"
}