#designerPdfViewer.py

# create dic  a:hgt
# for each block of text
# count letters
# get hgt of each letter finding max
# times number of letter by max height

def designerPdfViewer(h, word):
    letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_dict = dict(zip(letters,h))
    max_hgt = 0
    num_letters = len(word)
    for ltr in range(len(word)):
        if letter_dict.get(str(word[ltr])) > max_hgt:
            max_hgt = letter_dict.get(word[ltr])
    return num_letters * max_hgt
    


h = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]
word ='abcd'

print (designerPdfViewer(h, word))
