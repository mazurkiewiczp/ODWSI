from Crypto.PublicKey import RSA
import sys

with open(sys.argv[1]) as pub:
	pub_key = pub.read()

rsa_keys = RSA.importKey(pub_key)
encrypted = rsa_keys.encrypt("Ala ma kota", "")

szyfrogram = open(sys.argv[2],'w')
for c in encrypted:
	szyfrogram.write(c)
