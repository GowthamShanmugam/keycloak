from flask import Flask, request, jsonify
from flask_cors import CORS
from jose import jwt
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)

JWKS_URL = "http://localhost:8080/realms/rhoai/protocol/openid-connect/certs"
ISSUER = "http://localhost:8080/realms/rhoai"
EXPECTED_AZP = "client-app-2"  # Match your Keycloak clientId

jwks = requests.get(JWKS_URL).json()

@app.route('/protected', methods=['GET'])
def protected():
    auth = request.headers.get("Authorization", None)
    if not auth or not auth.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401

    token = auth.split(" ")[1]

    try:
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            issuer=ISSUER,
            options={"verify_aud": False}  # disable audience check
        )

        if payload.get("azp") != EXPECTED_AZP:
            return jsonify({"error": "Unauthorized client"}), 403

        return jsonify({"message": "✅ Token valid", "user": payload})

    except Exception as e:
        return jsonify({"error": str(e)}), 403

if __name__ == "__main__":
    app.run(host="app2.localhost", port=5002, debug=True)

