'''
rUns dOg
Dog RuNS

aWESOME is cODING

'''


in_string = 'aWESOME is cODING'

in_string = in_string.split(' ')
out_string = []
in_string.reverse()

for word in in_string:
	new_string = ''.join(c.lower() if c.isupper() else c.upper() for c in word)
	out_string.append(new_string)

print(' '.join(out_string))
	
 
