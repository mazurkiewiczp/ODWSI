from Crypto.PublicKey import RSA
import sys

rsa_keys = RSA.generate(1024)
priv_key = rsa_keys.exportKey()
pub_key = rsa_keys.publickey().exportKey()

pub = open(sys.argv[1],'w')
for c in pub_key:
	pub.write(c)

priv = open(sys.argv[2],'w')
for c in priv_key:
	priv.write(c)


	
