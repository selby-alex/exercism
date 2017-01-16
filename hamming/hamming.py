

def distance(s1,s2):
	#set hamming score to 0
	hamming = 0

	#analyze the lengths of 
	minlen = min(len(s1),len(s2))
	maxlen = max(len(s1),len(s2))

	for i in range(minlen):
		if s1[i] != s2[i]:
			hamming += 1
		else: continue

	hscore = hamming + (maxlen - minlen)

	return hscore





string1 = 'GGACGGATTCTG' 
string2 = 'AGGACGGATTCT'
#hamming(string1, string2)