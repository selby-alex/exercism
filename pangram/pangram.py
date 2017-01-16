

def is_pangram(string):
	alpha = ['a','b','c','d','e','f','g','h','i',
	'j','k','l','m','n','o','p','q','r','s','t',
	'u','v','w','x','y','z',]

	string = string.lower()

	for letter in str(string):
		if letter in alpha:
			alpha.remove(letter)
		else:
			continue

	if len(alpha) == 0:
		return True
	else:
		return False

string = is_pangram('Five quacking Zephyrs jolt my wax bed.')
print string