from pathlib import Path

import jwt
from cryptography.x509 import load_pem_x509_certificate


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    x509_certificate = load_pem_x509_certificate(
        Path("public_key.pem").read_text().encode()
    ).public_key()
    return jwt.decode(
        access_token,
        key=x509_certificate,
        algorithms=unverified_headers["alg"],
        audience="https://coffeemesh.io/orders",
    )


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pbyIsInN1YiI6NDU2NzY1NDQ1Njg3LCJhdWQiOiJodHRwczovL2NvZmZlZW1lc2guaW8vb3JkZXJzIiwiaWF0IjoxNjQxNDkzNTUzLCJleHAiOjE2NDE0MDcxNTMuNDIxMDk5fQ.g9zUMRuluHdtMcvN1BXC0sEMBgWGe5pz0vwlWrPqoN5W2M6-8LdPnhnkph1ZpkeqjfKp57_PVwVSsSzsMa2QzLbSllg8W6VCl8JWPJbYbrqqawnymdpCYIJTZ6TmoOqKzT6mMzmFjeopPoRjh8-t1lhKp_t8NsAaapD1Wdc3gLlZTmH6sYHW3DQSh0l6giBFCpLmVzfrpCfQiZ9M1YAPHlmkK-MKR8DUHm04TtujY4L7Se-fVSI_j4W-V1HGv8bRWbV0b0tmEsGlb7PrCry7UgT3yydp8sEVOul35kA38er2_fBibFqNtj83SASfG8JMDTgHtAhEjNWOD0EomZW4dA"

print(decode_and_validate_token(token))
