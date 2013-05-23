# Juan Marron.
# So this started as a simple encryption program and it turned into a library of modular arithmetic functions
# when I realized the decryption method needed more functions
# The following is an unfinished public key encryption program.

# Encrypts words according to Rabins Method. Takes words from command line as arguments in argv
# First each letter in word gets converted to ascii.
# Then (resulting number)^2 mod(public key) is the encryption of the word.
# Public key for the sake of this program is: 328419349
# Note the two prime factors we will be using that multiply to give 328419349 are 45343 and 7243. Note
# they are also congruent to 3mod4 (a necessary consideration)

import sys
import fractions as fr

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


arguments = sys.argv[1:]

for s in arguments:
	print "Encrypting " + "\"" + s + "\""
	print "Encrypted: " + str(encrypt(s))
