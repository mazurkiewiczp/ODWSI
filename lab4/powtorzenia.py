from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes

data = 'alamakotalamakotalamakotalamakot'
iv8 = get_random_bytes(8)
descbc = DES.new("key12345",DES.MODE_CBC, iv8)
desecb = DES.new("key12345",DES.MODE_ECB)
dencr1 = descbc.encrypt(data)
dencr2 = desecb.encrypt(data)

iv16 = get_random_bytes(16)
aescbc = AES.new("1234567890123456",AES.MODE_CBC, iv16)
aesecb = AES.new("1234567890123456",AES.MODE_ECB)
aencr1 = aescbc.encrypt(data)
aencr2 = aesecb.encrypt(data)

print("Szyfrowany tekst: " + data)
print("DES ECB: " + str(dencr2))
print("DES CBC: " + str(dencr1))
print("AES ECB: " + str(aencr2))
print("AES CBC: " + str(aencr1))

