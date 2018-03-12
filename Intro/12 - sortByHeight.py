"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

"""

def sortByHeight(a):
    array2 = sorted(list(filter(lambda x: x!=-1,a)))
    print (array2)
    
    indexVal = 0
    
    for i in range(0,len(a)):
        if (a[i] != -1):
            a[i] = array2[indexVal]
            indexVal+=1
    
    return a


'''
===Alternate Solution===
def sortByHeight(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l
'''
