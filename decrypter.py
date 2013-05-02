# Decrypter for use with encrypter.py. Encrypter codes the word into a number.
# Then you can run the number through the decrypter function in this code to find
# out what the word was
# Also contains some useful modular arithmetic functions

import sys
import fractions as fr

def congruentMod(x, y, modularBase):
	if ((x-y)%modularBase == 0):
		return True
	return False	

def testRelativelyPrime(num1, num2):
	if(fr.gcd(num1, num2) == 1):
		return True
	else:
		return False	

def getInverse(number, modularBase):
	if(not testRelativelyPrime(number, modularBase)):
		return 0 # false
	for i in range(modularBase):
		temp = (i * number)%modularBase
		if(temp == 1):
			return i		

def systemSolver(coeff1, mod1, coeff2, mod2):
	newCoeff = coeff2 - coeff1
	inv = getInverse(mod1, mod2)
	k = (newCoeff * inv) % mod2
	return (coeff1 + mod1*k)

def findCorrectRoot(r1, r2, r3, r4):	
	v = [r1, r2, r3, r4]
	for s in v:
		if(len(s) == 7):
			return r1


def decrypt(num):
	# First get square roots in Z45343, and then in Z7243	
	z1p = num**((45344)/4)%45343
	z2p = (-(num**((45344)/4)))%45343
	z3p =  num**((7244)/4)%7243
	z4p =  (-(num**((7244)/4)))%7243
	
	# Get the four square roots			
	r1 = str(systemSolver(z1p, 45343, z3p, 7243))
	r2 = str(systemSolver(z2p, 45343, z3p, 7243))
	r3 = str(systemSolver(z1p, 45343, z4p, 7243))
	r4 = str(systemSolver(z2p, 45343, z4p, 7243))
	return findCorrectRoot(r1, r2, r3, r4)

arguments = sys.argv[1:]

for i in arguments:
	print "Decrypting: " + str(i)
	print "Decrypted: " + str(decrypt(int(i)))
	
