'''
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''

year = 1996

leap = False

if year%4 == 0:
	leap = True
if year%400 != 0 and year%100 ==0:
	leap = False

return leap	

	
