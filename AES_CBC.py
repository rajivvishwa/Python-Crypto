from Crypto.Cipher import AES
from Crypto import Random
 
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]
 
class AESCipher:
    def __init__(self, key):
        self.key = key.decode("hex")
 
    def encrypt(self, pt):
        raw = pad(pt)
        iv = Random.new().read(BS);
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Return iv || ct
        return (iv + cipher.encrypt(pt)).encode("hex")
 
    def decrypt(self, ct):
        ct = ct.decode("hex")
        # Extract iv from ciphertext
        iv = ct[:BS]
        ct = ct[BS:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt(ct))
 
if __name__== "__main__":
    
    key = "01234567asd8"
    plaintext = 'abcdefghijkmnopqa1234s1222s';

    # AES key must be either 16, 24, or 32 bytes long. Hence padding with block_size
    key = pad(key).encode('hex')
    # AES Input strings must be a multiple of 16 in length. Hence padding with block_size
    plaintext = pad(plaintext)

    crypto = AESCipher(key)

    ciphertext = crypto.encrypt(plaintext)
    print "Cipher text - %s" % ciphertext

    plaintext = crypto.decrypt(ciphertext)
    print "Plain text - %s" % plaintext