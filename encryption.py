#encryption.py
import math


def encryption(s):
    s = s.replace(" ", "")
    encode = []
    length_mess = len(s)
    ngram=''
    result = ''
    row_len = math.floor(math.sqrt(length_mess))
    col_len = math.ceil(math.sqrt(length_mess))
    if row_len * col_len < length_mess:
        row_len += 1

    for letter in range(length_mess):
        ngram = ngram + s[letter]
        if len(ngram)>=col_len:
            encode.append(ngram)
            ngram = ''
    if ngram != '':
            encode.append(ngram)

    string_len = []
    for i in range(len(encode)):
        string_len.append(len(encode[i]))
        
    for col in range (col_len):
        for row in range (row_len):
            if col<string_len[row]:
                result = result + encode[row][col]
        result = result + ' '    
        
    result = result.rstrip()    
        

    return result


s = 'chillout'
print(encryption(s))

