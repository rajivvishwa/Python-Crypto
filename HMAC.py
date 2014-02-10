# http://pymotw.com/2/hmac/
# http://stackoverflow.com/questions/1306550

import hmac
import hashlib
import base64

class HMAC:
	def __init__(self, key, chunk_size):
		self.key = key.decode("hex")
		self.chunk_size = chunk_size

	def getHMAC_MD5(self, in_filename):
		dig = hmac.new(self.key)
		with open(in_filename, 'r') as in_file:
			while True:
				chunk = in_file.read(self.chunk_size)
				if len(chunk) == 0:
					break
				dig.update(chunk)
				return dig.hexdigest()

	def getHMAC_SHA_b64(self, msg):
		dig = hmac.new(self.key, msg, digestmod=hashlib.sha256).digest()
		return dig

if __name__ == '__main__':
	key = 'df0c97807d289c28bb1bb5d98442a434'
	chunk_size = 1024

	hmacObj = HMAC(key, chunk_size)

	# MD5 default
	print 'HMAC MD5-msg1	:', hmacObj.getHMAC_MD5('msg.txt')
	print 'HMAC MD5-msg2	:', hmacObj.getHMAC_MD5('msg2.txt')

	# SHA 256 example
	print 'HMAC SHA256		:', hmacObj.getHMAC_SHA_b64('test message').encode('hex')
	print 'HMAC SHA256 b64	:', base64.b64encode(hmacObj.getHMAC_SHA_b64('test message')).decode()
