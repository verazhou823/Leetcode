import sys
Height = [1,2,3]
def subLength(Height):
    if len(Height)<=1:
        return 0
    minimum = sys.maxint
    maximum = -sys.maxint-1
    for i in range(len(Height) - 1) :
        if Height[i] > Height[i + 1]:
            if Height[i] > maximum:
                maximum = Height[i]
            if Height[i + 1] < minimum:
                minimum = Height[i + 1]
    if Height[-1] < Height[-2]:
        if Height[-1] < minimum :
            minimum = Height[-1]
    if minimum == sys.maxint:
        return 0
    i = 0
    while(i < len(Height) and Height[i] < minimum):
        i += 1
    j = len(Height)-1
    while(j>=0 and Height[j] > maximum):
        j -= 1
    return j-i+1
print(subLength(Height))

