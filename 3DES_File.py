# Reference - http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/

import os
from Crypto.Cipher import DES3
from Crypto import Random

class DES3Cipher:

    def __init__(self, key, iv, chunk_size):
        self.key = key.decode("hex")
        self.iv = iv
        self.chunk_size = chunk_size

    def encrypt_file(self,in_filename):
        des3 = DES3.new(self.key, DES3.MODE_CFB, self.iv)

        with open(in_filename, 'r') as in_file:
            with open(in_filename.replace('txt','enc'), 'w') as out_file:
                while True:
                    chunk = in_file.read(self.chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)
                    out_file.write(des3.encrypt(chunk))

    def decrypt_file(self,in_filename):
        des3 = DES3.new(self.key, DES3.MODE_CFB, self.iv)

        with open(in_filename, 'r') as in_file:
            with open(in_filename.replace('enc','dec'), 'w') as out_file:
                while True:
                    chunk = in_file.read(self.chunk_size)
                    if len(chunk) == 0:
                        break
                    out_file.write(des3.decrypt(chunk))

if __name__== "__main__":

    key  = "df0c97807d289c28bb1bb5d98442a434"
    iv = Random.get_random_bytes(8)
    chunk_size = 8192

    crypto = DES3Cipher(key, iv, chunk_size)
    crypto.encrypt_file('msg.txt')
    crypto.decrypt_file('msg.enc')

    with open('msg.txt', 'r') as f: print 'Message (PlainText): %s' % f.read()
    with open('msg.enc', 'r') as f: print 'Message (Encrypted): %s' % f.read().encode('hex')
    with open('msg.dec', 'r') as f: print 'Message (Decrypted): %s' % f.read()
