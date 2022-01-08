from datetime import datetime, timedelta
from pathlib import Path

import jwt
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.coffeemesh.io",
        "sub": 456765445687,
        "aud": "https://coffeemesh.io/orders",
        "iat": now,
        "exp": (now - timedelta(hours=24)).timestamp(),
    }

    private_key_text = Path("private_key.pem").read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(), password=None
    )

    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")


print(generate_jwt())
