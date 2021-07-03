'''
n = 5

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

if __name__ == '__main__':
    
    records = []
        
    for n in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        records.append(student)
    '''
records = [['a',-50],['b',-50],['c',-50],['d',50]]
records.sort(key=lambda x: x[1])

lowest = records[0][1]

records.pop(0)
records2 =[]
while lowest ==  records[0][1]:
	records.pop(0)
	second = records[0][1] 
while len(records) > 0 and records[0][1]== second:
	records2.append(records[0][0])
	records.pop(0)
		
records2.sort()
for name in records2:
	print(name)
        
