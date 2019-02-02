#-*- coding: utf-8 -*-
import struct

#行程长度压缩之python版本
def RLE_enc(filename):
	orgf = open(filename, "rb")
	b = orgf.read()
	byteslen = len(b)
	if byteslen <= 0:
		print(filename+" is null")
		return
	orgf.close()
	print(filename+" len "+str(byteslen))
	encb = bytearray()
	ch = b[0]
	encb.append(1)
	encb.append(ch)
	nch=1
	num = 1
	for i in xrange(1,byteslen):
		if ch == b[i]:
			num = num + 1
		else:
			encb[2*nch-2]=num
			encb[2*nch-1]=ch
			ch=b[i]
			encb.append(0)
			encb.append(0)
			nch = nch + 1
			num=1
			pass
		pass
	encb[2*nch-2]=num
	encb[2*nch-1]=ch
	encf = open(filename+".rle", "wb")
	encf.write(encb)
	encf.close()
	pass

def RLE_dec(filename):
	idx = filename.find(".rle")
	if idx < 0:
		return
	impressname = filename[0:idx]

	orgf = open(filename, "rb")
	orgdat = orgf.read()
	orgf.close()
	orglen = len(orgdat)
	if orglen <= 0:
		return
	dlen = 0
	decb = bytearray()
	while dlen < orglen:
		nc = orgdat[dlen+0]
		ch = orgdat[dlen+1]
		num = ord(nc)
		for i in xrange(0,num):
			decb.append(ch)
			pass
		dlen = dlen + 2
		if dlen >= orglen:
			break
		pass
	if len(decb) <= 0:
		print("no dec data")
		return
	decf = open(impressname, "wb")
	decf.write(decb)
	decf.close()
	pass

if __name__ == "__main__":
	RLE_dec("test.py.rle")