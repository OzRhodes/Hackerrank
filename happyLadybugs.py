#happyLadybugs(b).py


def happyLadybugs(b):
    happy = False
    answer = 'YES'
    bugs = []
    for c in b:
        bugs.append(c)
    bugs = list(set(bugs))
 
    if len(bugs)==1 and '_' in b:                     # done
            return 'YES'
    if len(bugs)==1 and len(b)<2 and '_' not in bugs: # done
        return 'NO'

    if '_' in b:
        happy = True
        for c in bugs:
            if b.count(c) < 2 and  c !='_':
                return 'NO'
    else:
        happy = False
        for c in range(len(b)-1):
            if b[c] !=  b[c+1] and happy == False:
                return 'NO'
            elif b[c] ==  b[c+1]:
                happy = True
            else:
                happy = False
                 
    if happy == False:
        answer = 'NO'
    return answer


b ='B_RRBR'
print(happyLadybugs(b))