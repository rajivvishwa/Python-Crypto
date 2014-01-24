from Crypto.Cipher import DES
from Crypto import Random

BS = DES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

class DESCipher:
    def __init__(self, key):
        self.key = key.decode("hex")

    def encrypt(self, pt):
        pt = pad(pt)
        iv = Random.new().read(DES.block_size);
        cipher = DES.new(self.key, DES.MODE_CFB, iv)
        # Return iv || ct
        return (iv+cipher.encrypt(pt)).encode('hex')
 
    def decrypt(self, ct):
        ct = ct.decode("hex")
        # Extract iv from ciphertext
        iv = ct[:BS]
        ct = ct[BS:]
        cipher = DES.new(self.key, DES.MODE_CFB, iv)
        return unpad(cipher.decrypt(ct))

if __name__== "__main__":
    
    key = '012345678'
    plaintext = 'abcdefghijkmnopqa';
    
    key = key.encode('hex')
    # Truncate hex encoded key to block size, so 2x BS
    key=key[:2*BS]

    crypto = DESCipher(key)
    
    ciphertext = crypto.encrypt(plaintext)
    print "Cipher text - %s" % ciphertext

    plaintext = crypto.decrypt(ciphertext)
    print "Plain text - %s" % plaintext