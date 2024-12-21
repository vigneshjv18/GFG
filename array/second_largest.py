def getSecondLargest(arr):
    remove_duplicate = list(set(arr))
    remove_duplicate.sort(reverse=True)
    if len(remove_duplicate) > 1:
        return remove_duplicate[1]
    else:
        return -1
    
arr = [12, 35, 1, 10, 34, 1]
print(getSecondLargest(arr))

