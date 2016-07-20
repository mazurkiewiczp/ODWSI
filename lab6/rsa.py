from Crypto.PublicKey import RSA


rsa_keys = RSA.generate(1024)
pub_key = rsa_keys.exportKey()
priv_key = rsa_keys.publickey().exportKey()

encrypted = rsa_keys.encrypt("Ala ma kota", "")

print (str(rsa_keys.decrypt(encrypted)))

print(priv_key)
