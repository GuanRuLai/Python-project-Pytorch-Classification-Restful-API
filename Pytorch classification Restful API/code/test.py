import requests

# test health checker
health_response = requests.get("http://127.0.0.1:8000/health")
print(health_response.json())

# test prediction endpoint
data = {"title": "實習生"}
predict_response = requests.post("http://127.0.0.1:8000/predict/title", json=data)
print(predict_response.json())
