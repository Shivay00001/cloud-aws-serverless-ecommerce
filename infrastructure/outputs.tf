output "api_url" {
  description = "URL of the API Gateway"
  value       = aws_apigatewayv2_api.http_api.api_endpoint
}
