import requests

# Define the API endpoint
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

# Make a GET request
response = requests.get(API_URL)

# Print the response details
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Validate the response
assert response.status_code == 200, "Status code is not 200!"
assert response.json()["id"] == 1, "ID does not match!"
