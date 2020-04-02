#angryProfessor.py




def angryProfessor(k, a):
    class_size = 0
    for arrival in range(len(a)):
        if a[arrival] <= 0:
            class_size += 1
    if class_size < k:
        return 'YES'  # Cancelled
    else:
        return 'NO'   # Proceeds



k = 3
a=[-1,-3,4,2]

print (angryProfessor(k, a))