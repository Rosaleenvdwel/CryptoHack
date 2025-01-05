from Crypto.Util.number import long_to_bytes

ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
decrypted_int = ct  #since the ciphertext contains the flag I only really need this value
decrypted_bytes = long_to_bytes(decrypted_int)

print(decrypted_bytes)
