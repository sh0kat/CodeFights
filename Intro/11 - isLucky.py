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
