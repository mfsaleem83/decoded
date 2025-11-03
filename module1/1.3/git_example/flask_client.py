
import requests

# Valid request
response = requests.post("http://localhost:8100/echo",
                         json={"message": "Hello,Fahad!"})
print("Valid response:", response.status_code, response.json())

# TODO: Try sending invalid input (e.g. {"text": "Hi"}) and print the status + response
response = requests.post("http://localhost:8100/echo", json={"text": "Hi"})
print("In-Valid response:", response.status_code, response.json())

# Test the /status endpoint
response = requests.get("http://localhost:8100/status")
print("Status check:", response.status_code, response.json())

response = requests.get("http://localhost:8100/greet?name=fahad")
print("Status check:", response.status_code, response.json())

response = requests.get("http://localhost:8100/greet?name=")
print("Status check:", response.status_code, response.json())

response = requests.get("http://localhost:8100/greet")
print("Status check:", response.status_code, response.json())

response = requests.get("http://localhost:8100/greet?name=saleem")
print("Status check:", response.status_code, response.json())
