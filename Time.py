def giveTime(time):
    def travel(time,answer,result):
        if len(answer) == 4:
            result.append(answer)
        for i in range(len(time)):
            if i!=len(time)-1:
                travel(time[0:i]+time[i+1:],answer+str(time[i]),result)
            else:
                travel(time[0:i],answer+str(time[i]),result)
    answer = ""
    result = []
    travel(time,answer,result)
    def valid(s):
        return int(s[0])*10+int(s[1])<=23 and int(s[2])*10+int(s[3])<=59
    result = sorted(result)
    for i in range(len(result)-1,-1,-1):
        if valid(result[i]):
            return result[i]
    return -1
print(giveTime([0,0,0,0]))
