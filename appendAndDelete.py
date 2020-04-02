#appendAndDelete.py


def appendAndDelete(s, t, k):
  
    # A common string
    if s == t:
        if k%2 == 0 or k>4:
            return 'Yes'
        else:
            return 'No' 
    #create lists
    s_list=[]
    t_list = []
    for letter in s:
        s_list.append(letter)
    for letter in t:
        t_list.append(letter)
    
    # find length of common chars
    common_length = 0
    if len(s_list)>len(t_list):
        for lst in range(len(t_list)):
            if s_list[lst] == t_list[lst]:
                common_length += 1
    elif len(s_list)<len(t_list):
        for lst in range(len(s_list)):
            if t_list[lst] == s_list[lst]:
                common_length += 1
                
    if((len(s_list)+len(t_list))-2*common_length) > k:
        return 'No'
    elif (len(s_list)+len(t_list)-2*common_length)%2 == k%2:
        return 'Yes'

    elif(len(s_list)+len(t_list)-k) <0:
        return 'Yes'
    else:
        return 'No'
    

s = 'qwerasdf'
t = 'qwerbsdf'
k = 6

print (appendAndDelete(s, t, k))