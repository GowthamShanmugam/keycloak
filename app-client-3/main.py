import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

KEYCLOAK_TOKEN_URL = "http://localhost:8080/realms/rhoai/protocol/openid-connect/token"
CLIENT_ID = "client-app-3"  # Match your Keycloak clientId
CLIENT_SECRET = ""

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    print(f"Login attempt with username: {username}")
    print(f"Login attempt with password: {password}")
    payload = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": username,
        "password": password,
    }

    response = requests.post(KEYCLOAK_TOKEN_URL, data=payload)
    print(f"Response status code: {response.content}")

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="app1.localhost", port=5003, debug=True)
