
'''
test list
shopping_list = [['BANANA FRIES',  12],['POTATO CHIPS',  30],['APPLE JUICE', 10],['CANDY', 5],['APPLE JUICE', 10],['CANDY',  5],['CANDY',  5],['CANDY',  5],['POTATO CHIPS', 30]]
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

my_dict = OrderedDict()
shopping_list =[]
for n in range(int(input())):
    trans = []
    sale = input().split(' ')
    price = float(sale[-1])
    del sale[-1]
    item = ' '.join(sale)
    trans.append(item)
    trans.append(price)
    shopping_list.append(trans)

for item in shopping_list:
    if item[0] not in my_dict:
        my_dict[item[0]] = item[1]
    else:
        my_dict[item[0]] = my_dict[item[0]] + item[1]

for key, total in my_dict.items():
    print(key, (int(total)))
