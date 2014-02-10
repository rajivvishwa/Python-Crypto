import os
from Crypto.Hash import MD5

class MD5Hash:
	def __init__(self, chunk_size):
		self.chunk_size = chunk_size

	def getHash(self, filename):
	    h = MD5.new()
	    with open(filename, 'rb') as f:
	        while True:
	            chunk = f.read(self.chunk_size)
	            if len(chunk) == 0:
	                break
	            h.update(chunk)
	    return h.hexdigest()


if __name__== "__main__":
	chunk_size = 8192

	md5hash = MD5Hash(chunk_size)
	print md5hash.getHash('msg.txt')