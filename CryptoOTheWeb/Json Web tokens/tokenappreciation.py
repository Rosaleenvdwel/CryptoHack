import base64
import json

def decode_jwt(token):
    
    header, payload, _ = token.split('.')

    #decodes from base64
    decoded_header = base64.urlsafe_b64decode(header + '==').decode('utf-8')
    decoded_payload = base64.urlsafe_b64decode(payload + '==').decode('utf-8')

    return decoded_header, decoded_payload

if __name__ == "__main__":
    jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"
    
    header, payload = decode_jwt(jwt_token)
    
    print("Header:", header)
    print("Payload:", payload)