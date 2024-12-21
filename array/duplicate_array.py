class Solution:
    def findDuplicates(self, arr):
        arr.sort()
        duplicate = []
        seen = set()
        for num in arr:
            if num in seen:
                duplicate.append(num)
            else:
                seen.add(num)
        print(duplicate)        
        return duplicate 

arr = [12, 35, 1, 12, 34, 1]
Solution().findDuplicates(arr)