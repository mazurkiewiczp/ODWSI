from Crypto.PublicKey import RSA
import sys

with open(sys.argv[1]) as priv:
	priv_key = priv.read()

rsa_priv_key = RSA.importKey(priv_key)


with open(sys.argv[2]) as msg:
	szyfrogram = msg.read()

print(rsa_priv_key.decrypt(szyfrogram))
