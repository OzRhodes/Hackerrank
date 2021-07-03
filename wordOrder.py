'''
test data
n = 4
words=['bcdef', 'abcdefg', 'bcde', 'bcdef']
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

words = []
for n in range(int(input())):
    
    words.append(input())

word_dict ={}
for word in words:
    if word not in word_dict:
        word_dict[word]=1
    else:
        word_dict[word] +=1
sorted(word_dict.items(), key=lambda x: x[1])
print(len(word_dict))
for word in word_dict:
    print(word_dict[word], end =' ')
	
