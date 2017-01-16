

def encode(string, counter = 0):
	encoding = []
	shortcode = ''

	for letter in string:
		encoding.append(letter)

	while counter < len(encoding):
		x = encoding[counter]
		y = 0
		for letter in encoding[counter:]:
			if letter == x:
				counter += 1
				y += 1
			else:
				break
		if y == 1:
			shortcode += str(x)
		else:
			shortcode += str(y)
			shortcode += str(x)
			print(shortcode)

	return shortcode

def decode(string):
	counter = 0

#def decode(string):


encode('⏰⚽⚽⚽⭐⭐⏰')
#decode('12WB12W3B24WB')