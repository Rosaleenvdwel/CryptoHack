import requests
from Crypto.Cipher import AES
import hashlib


wordlist_url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"


ciphertext = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")

#streams wordlist from url
response = requests.get(wordlist_url, stream=True)

#iterate over the wordlist
for word in response.iter_lines():
    word = word.decode('utf-8').strip()

    #md5 hashed
    key = hashlib.md5(word.encode()).digest()

    #decrypt the ciphertext using AES in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)

    
    try:
        plaintext = decrypted.decode('utf-8')
        if "FLAG" in plaintext:
            print(f"Success! The password is: {word}")
            print(f"Decrypted text: {plaintext}")
            break
        
    except (ValueError, UnicodeDecodeError):

        continue