# Lambda container image for the ecommerce handlers.
# Build: docker build -t ecommerce-lambda .   Deploy: push to ECR, create Lambda from image.
FROM public.ecr.aws/lambda/python:3.11
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/handlers/ ./
# Handlers: create_order.handler, get_product.handler (set per-function in AWS)
CMD ["create_order.handler"]
