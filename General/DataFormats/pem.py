from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail.pem', 'rb') as pem_file:
    key = RSA.import_key(pem_file.read())

d = key.d
print(d)  
