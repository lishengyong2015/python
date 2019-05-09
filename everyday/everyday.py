#-*- coding: utf-8 -*-
import math
import time

def isPrime(num):
	if num <= 3:
		return num > 1
		pass
	if (num % 6 != 1) and (num % 6 != 5):
		return False
		pass
	sqrts = int(math.sqrt(num))
	i=5
	while i <= sqrts:
		if (num % i == 0) or (num % (i + 2) == 0):
			return False
			pass
		i = i + 6
		pass
	return True
	pass

starttime = time.time()
cnt=0
lastprime=0
while True:
	curtime = time.time()
	if curtime - starttime > 10.0:
		break
		pass
	#print(str(curtime-starttime))
	if isPrime(cnt):
		lastprime=cnt
		#print(str(cnt))
		pass
	cnt=cnt+1
	pass

print("lastprime is "+str(lastprime))