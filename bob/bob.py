#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
	if what.isupper() and what.endswith('!'):
		return('Whoa, chill out!')
	elif what.isupper():
		return('Whoa, chill out!')
	elif what.strip().endswith('?'):
		return('Sure.')
	elif what.endswith('.') or what.endswith('!'):
		return('Whatever.')
	elif len(what.strip()) == 0:
		return('Fine. Be that way!')
	else:
		return 'Whatever.'


#    return


x = hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
print(x)

