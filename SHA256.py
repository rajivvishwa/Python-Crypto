from Crypto.Hash import SHA256
# or
import hashlib

string = 'Hello World'

# pycryto
h = SHA256.new()
h.update('Hello ')
h.update('World')
print h.hexdigest()	

# hashlib
h = hashlib.sha256(string)
print h.hexdigest()	