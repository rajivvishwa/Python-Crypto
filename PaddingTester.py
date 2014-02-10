'''
URL: https://pypi.python.org/pypi/Padding
Description: Padding methods for password based encryption
'''

import Padding

msg = 'this'
DES_BS = Padding.DES_blocksize
AES_BS = Padding.AES_blocksize


print "DES has fixed block size of %d bits = %d bytes" % (DES_BS*8, DES_BS)

padded_msgDES = Padding.appendPadding(msg, DES_BS)
print padded_msgDES.encode('hex'), len(padded_msgDES)

msgDES = Padding.removePadding(padded_msgDES)
print msgDES, len(msgDES)

print 
print "AES has fixed block size of %d bits = %d bytes" % (AES_BS*8, AES_BS)

padded_msgAES = Padding.appendPadding(msg)
print padded_msgAES.encode('hex'), len(padded_msgAES)

msgAES = Padding.removePadding(padded_msgAES)
print msgAES, len(msgAES)