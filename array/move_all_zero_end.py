arr = [0, 5, 0, 0 ,4]
"""
non_zero =[]
add_zero =[]
for num in arr:
    if num != 0:
        non_zero.append(num)
    else:
        add_zero.append(num)
print(non_zero + add_zero)
"""
# swap array
count =0

for item in range(len(arr)):
    if arr[item] !=0:
        arr[item],arr[count] = arr[count], arr[item] # 3,3 = 3,3
        # arr[count] = arr[item]
        count +=1
print(arr)