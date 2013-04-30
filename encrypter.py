# Juan Marron.
# The following is an unfinished encryption program. Mostly a test to get to know how to use github

# Encrypts words according to Rabins Method. Takes words from command line as arguments in argv
# First each letter in word gets converted to ascii.
# Then (resulting number)^2 mod(public key) is the encryption of the word.
# Public key for the sake of this program is: 328419349
# Note the two prime factors we will be using that multiply to give 328419349 are 45343 and 7243. Note
# they are also congruent to 3mod4.

import sys

def encrypt(word):
	word = word.lower()	
	pkey = 328419349
	coded = ""
	temp = ""	
	for c in word:
		temp = str(ord(c)-96)	
		if (ord(c) - 96) < 10:
			temp = '0' + temp	
		coded+=temp	
	coded = int(coded)

	return (coded**2)%pkey

def decrypt(num):
	# First get square roots in Z45343, and then in Z7243	
	z1p = num**((45344)/4)%45343
	z2p = (-(num**((45344)/4)))%45343
	z3p =  num**((7244)/4)%7243
	z4p =  (-(num**((7244)/4)))%7243
	# Then do Chinese Remainder theorem to get the four roots
	# Have not gotten around to doing this yet	

arguments = sys.argv[1:]
for s in arguments:
	print "Encrypting " + "\"" + s + "\""
	print "Encrypted: " + str(encrypt(s))
