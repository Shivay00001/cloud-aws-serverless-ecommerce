variable "aws_region" {
  description = "AWS Region to deploy to"
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  default     = "dev"
}
