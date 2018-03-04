"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
"""

import math
def checkPalindrome(inputString):
    
    flag = False
    length= len(inputString)
    mid = math.ceil(length/2)
    for i in range(0,mid):
        if inputString[i] == inputString[length-i-1]:
            flag = True
        else:
            flag = False
            break;
    return flag
        