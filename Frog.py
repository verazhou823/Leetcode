import sys
X = 7
A = [1,3,1,1,1]
D = 3

def steps(A,X,D):
    if X<=D:
        return 0
    if len(A)+D-1<X:
        return -1
    if A[0]<=D and A[0]+D>=X:
        return 0
    dp = [-1 for i in range(X)]
    dp[0] = 0
    for i in range(len(A)):
        if A[i]<X:
            if dp[A[i]] == -1:
                dp[A[i]] = i
            else:
                dp[A[i]] = min(dp[A[i]],i)
    for i in range(X):
        if i <= D:
            pass
        else:
            if dp[i] != -1:
                flag = 0
                minimum = sys.maxint
                for j in range(1,D+1):
                    if dp[i-j] == -1:
                        pass
                    elif dp[i-j] <= dp[i]:
                        flag = 1
                        break
                    elif dp[i-j]>dp[i] and dp[i-j]<minimum:
                        minimum = dp[i-j]
                if flag == 0 and minimum == sys.maxint:
                    dp[i] = -1
                elif flag == 0 :
                    dp[i] = minimum
    print(dp)
    minimum = sys.maxint
    for i in range(1,D+1):
        if dp[-i] != -1 and dp[-i] < minimum:
            minimum = dp[-i]
    return minimum if minimum != sys.maxint else -1
print(steps(A,X,D))


