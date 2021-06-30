'''
# test of 2 inputs
#x = int ( raw_input()) 
#y = int ( raw_input()) 
#n = int ( raw_input()) 

x = 3
y = 3
n = 3

arr = [] 
p = 0 
for i in range ( x + 1 ): 
	for j in range( y + 1): 
		if i+j != n: 
			arr.append([]) 
			arr[p] = [ i , j ] 
			p+=1 
print (arr)

# Code using list comprehensions: 

#x = int ( raw_input()) 
#y = int ( raw_input()) 
#n = int ( raw_input()) 

print ([[ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])
'''
# 3 inputs

#x = int(raw_input())
#y = int(raw_input())
#z = int(raw_input())
#n = int(raw_input())

x = 3
y = 3
z = 3
n = 3

# Non List Comprehensions 
output = [];
arr = [];
for X in range(x+1):
	for Y in range(y+1):
		for Z in range(z+1):
			if X+Y+Z != n:
				abc = [X,Y,Z]
				output.append(abc)
print(output)
print(' ')

print ([[ i, j, k] for i in range( x + 1) for j in range( y + 1)  for k in range (z + 1) if ( ( i + j + k) != n )])

