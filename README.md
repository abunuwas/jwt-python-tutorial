Working with JWTs in Python

Code for my video tutorial [Working with JWTs in Python](https://youtu.be/VRn8cPc7B_w).

JWTs are JSON documents which contain claims. We distinguish two types of JWTs: ID tokens and access tokens.

ID tokens are tokens which carry identifying information about a user, such as their name, username, email, date of birth, and other details. You should NEVER use an ID token to validate access to an API.

Access tokens are tokens which contain claims about the right of a user to access an API or a resource. These are the tokens that we must use to validate access to an API.

The standard claims of an access token are:

• `iss` (issuer): identifies the authorization server that issued the JWT.
• `sub` (subject): identifies the subject of the JWT, i.e. the user sending the request to the server.
• `aud` (audience): indicates the recipient for which the JWT is intended. This is our API server.
• `exp` (expiration time): when the JWT expires.
• `nbf` (not before time): time before which the JWT must not be accepted.
• `iat` (issued at time): when the JWT was issued.
• jti (JWT ID): a unique identifier for the JWT.

JWTs are commonly signed using the `HS256` and the `RS256` algorithms. `HS256` uses a secret to encrypt the token, while `RS256` uses a private/public key to sign the token. We use this information to apply the right algorithm to verify the token’s signature.

In the video, I demonstrate how to produce and validate JWTs using [PyJWT](https://github.com/jpadilla/pyjwt). To generate a token using PyJWT, we use the following function:

```python
jwt.encode(payload=payload, key='secret', algorithm=’HS256')
```

I also use Python's [cryptography library](https://github.com/pyca/cryptography) to load the token's signing certificates.

Some of the articles and websites mentioned in the video are: 
- The RFC "JSON Web Token (JWT)" (https://datatracker.ietf.org/doc/html/rfc7519). This is the reference for everything you want to know about JWTs.
- [https://jwt.io](https://jwt.io). This website is great for inspecting and validating JWTs.
- The RFC "The Base16, Base32, and Base64 Data Encodings" (https://datatracker.ietf.org/doc/html/rfc4648). This RFC describes how base encoding works, including base64url encoding, which is the type of encoding used for JWTs.
- JWT claims website: https://www.iana.org/assignments/jwt/jwt.xhtml. This website contains the list of all standard claims you can find in JWTs.

To learn more about JWTs, I also recommend Prabath Siriwardena's ["JWT, JWS and JWE for Not So Dummies! (Part I)"](https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3).

In case you're unable to generate the signing certificates with the openssl command as shown in the video, the repo includes an exmaple of private and public keys.

The command for generating the signing certificates is:

```bash
openssl req -x509 -nodes -newkey rsa:2048 -keyout private_key.pem -out public_key.pem -subj "/CN=jwt-turorial"
```
