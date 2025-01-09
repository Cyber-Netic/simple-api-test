import requests

# Test a simple API endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
