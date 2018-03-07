"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
"""

def isLucky(n):
    str1 = str(n)
    sum1=0
    sum2=0
    half = int(len(str1)/2)
    for i in range(0,half):
        sum1+=int(str1[i])
    for j in range(half,half*2):
        sum2+=int(str1[j])
    return sum1 == sum2

#def isLucky(n):
#    s = str(n)
#    pivot = len(s)//2
#    left, right = s[:pivot], s[pivot:]
#    return sum(map(int, left)) == sum(map(int, right))
