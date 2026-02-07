# Cloud AWS Serverless E-commerce

[![Terraform](https://img.shields.io/badge/Terraform-1.6-623CE4.svg)](https://www.terraform.io/)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900.svg)](https://aws.amazon.com/lambda/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **scalable serverless e-commerce backend** built on AWS. This repository uses Terraform for Infrastructure as Code (IaC) to provision a fully serverless architecture consisting of API Gateway, Lambda functions, and DynamoDB tables.

## 🚀 Features

- **Serverless Architecture**: Zero server management with AWS Lambda and API Gateway.
- **Infrastructure as Code**: Complete AWS environment provisioning using Terraform.
- **NoSQL Database**: DynamoDB for high-performance, single-digit millisecond latency.
- **RESTful API**: Clean API design for product management and order processing.
- **Scalability**: Auto-scaling capabilities inherent to the serverless design.
- **Cost Efficient**: Pay-per-use pricing model optimized for variable traffic.

## 📁 Project Structure

```
cloud-aws-serverless-ecommerce/
├── infrastructure/       # Terraform IaC definitions
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── src/
│   └── handlers/         # Lambda function code
│       ├── create_order.py
│       └── get_product.py
├── requirements.txt
└── Makefile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/cloud-aws-serverless-ecommerce.git

# Initialize Terraform
cd infrastructure
terraform init

# Deploy Infrastructure
terraform apply -auto-approve
```

## 📄 License

MIT License
