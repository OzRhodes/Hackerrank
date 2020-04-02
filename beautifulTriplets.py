#beautifulTriplets.py

def beautifulTriplets(d, arr):
    bt_cnt = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            bt_cnt +=1
    return bt_cnt 




d = 3
arr=[1,2,4,5,7,8,10]
print(beautifulTriplets(d, arr))