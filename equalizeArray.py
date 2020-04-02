#equalizeArray.py


def equalizeArray(arr):
    freq = []
    for num in range(1, max(arr)+1):
        freq.append(arr.count(num))
    answer =  (len(arr)-max(freq))

    return answer



arr = [1,2,3,1,2,3,3,3]
print(equalizeArray(arr))