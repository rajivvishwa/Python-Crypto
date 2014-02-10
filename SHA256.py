from Crypto.Hash import SHA256
# or
import hashlib

string = 'Hello World'

class SHA256Hash:
	def __init__(self, method):
		self.method = method

	def getHash(self):
		print "-- Using", method, "---"
		if(method == 'pycryto'):
			h = SHA256.new()
			h.update('Hello ')
			h.update('World')
			return h.hexdigest()

		elif(method == 'hashlib'):
			h = hashlib.sha256(string)
			return h.hexdigest()
		else:
			print 'Error !'

if __name__== "__main__":

	method = 'hashlib'
	sha256 = SHA256Hash(method)
	print sha256.getHash()