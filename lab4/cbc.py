from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes

msg = 'alamakotalamakotalamakotalamakot'
desECB = DES.new("key12345", DES.MODE_ECB)
aesECB = AES.new("1234567890123456", AES.MODE_ECB)
iv8 = get_random_bytes(8)
iv16 = get_random_bytes(16)

desCBC = DES.new("key12345", DES.MODE_CBC, iv8)
aesCBC = AES.new("1234567890123456", AES.MODE_CBC, iv16)

def encryptBlock(block, vector, ecb, N):
	bl = b''
	for i in range(N):
		bl +=bytes([ord(block[i]) ^ vector[i]])
	return ecb.encrypt(bl)

def encryptCBC(data, iv, ecb, N):
	blocks = [data[i:i+N] for i in range(0, len(data), N)]
	encrypted = b''
	for i in range(len(blocks)):
		iv = encryptBlock(blocks[i],iv,ecb,N)
		encrypted += iv
	return encrypted

print("DES CBC z biblioteki: ",end='')
print(desCBC.encrypt(msg))
print("DES CBC zaimplementowany: ",end='')
print(encryptCBC(msg,iv8,desECB,8))
print()
print("AES CBC z biblioteki: ",end='')
print(aesCBC.encrypt(msg))
print("AES CBC zaimplementowany: ",end='')
print(encryptCBC(msg,iv16,aesECB,16))
