variable "instance_type" {
  description = "EC2 Instance Type"
  default     = "t2.large"
}

variable "key_name" {
  description = "AWS Key Pair Name"
  default     = "assign.key"
}