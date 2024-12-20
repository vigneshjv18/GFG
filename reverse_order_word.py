# User function Template for python3

class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        separate = s.split(' ') 
        reverse_list = [val for val in separate[::-1] if val != ''] 
        if reverse_list:  # Ensure reverse_list is not empty
            reverse = " ".join(reverse_list)
        else:
            reverse = ""
        
        return reverse
            
        # code here 
solution = Solution()

# Test cases
test_cases = [
    "  Hello   world   Python  ",  # Normal case with extra spaces
    "Hello world",                # No extra spaces
    "     ",                      # Only spaces
    "",                           # Empty string
    "OneWord",                    # Single word
    "Word1  Word2 Word3  ",       # Mixed spacing
]

for i , test_case in enumerate(test_cases):
    result = solution.reverseWords(test_case)
    print(f"Test Case {i}: Input: '{test_case}' | Output: '{result}'")


#{ 
 # Driver Code Starts
 
 
"""_summary_
 
class Main:
    if __name__ == "__main__":
        t = int(input())  # Read the number of test cases

        for _ in range(t):
            s = input().strip()  # Read the input string

            # Remove surrounding quotes from the string
            str_ = s[1:-1]

            obj = Solution()  # Create an object of the Solution class
            ans = obj.reverseWords(str_)  # Reverse the words in the string

            # Print the result with surrounding quotes
            print(f'"{ans}"')

# } Driver Code Ends

       """