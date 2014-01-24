from Crypto.Cipher import DES

BS = DES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

class DESCipher:
    def __init__(self, key):
        self.key = key.decode("hex")

    def encrypt(self, pt):
        pt = pad(pt)
        cipher = DES.new(self.key, DES.MODE_ECB)
        return (cipher.encrypt(pt)).encode('hex')
 
    def decrypt(self, ct):
        ct = ct.decode("hex")
        cipher = DES.new(self.key, DES.MODE_ECB)
        return unpad(cipher.decrypt(ct))

if __name__== "__main__":
    
    key = '012345678'
    plaintext = 'abcdefghijkmnoasdsdap';
    
    key = key.encode('hex')
    # Truncate hex encoded key to block size, so 2x BS
    key=key[:2*BS]

    crypto = DESCipher(key)
    
    ciphertext = crypto.encrypt(plaintext)
    print "Cipher text - %s" % ciphertext

    plaintext = crypto.decrypt(ciphertext)
    print "Plain text - %s" % plaintext