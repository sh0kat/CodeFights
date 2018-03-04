"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def almostIncreasingSequence(s):  
    return 3> sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))

#   sum1 = 0
#    for i, j, k in zip(s, s[1:], s[2:] + [10**6]):
#        print(i,j,k)
#        print (i>=j,i>=k)
#        print((i >= j) + (i >= k))
#        sum1 += (i >= j) + (i >= k)
#    print(sum1)
#    return 3 > sum1