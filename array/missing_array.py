#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        arr = set(arr)
        for item in range(1,len(arr)+2):
            if item not in arr:
                return item
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# t = int(input())
# for _ in range(0, t):
#     arr = list(map(int, input().split()))
#     s = Solution().missingNumber(arr)
#     print(s)

#     print("~")
# } Driver Code Ends