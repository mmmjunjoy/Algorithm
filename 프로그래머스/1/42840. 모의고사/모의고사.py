def solution(answers):

    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    resulta=0
    resultb =0
    resultc=0
    
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            resulta +=1
        if b[i%8] == answers[i]:
            resultb +=1
        if c[i%10] == answers[i]:
            resultc +=1
        
    print(resulta,resultb,resultc)
    returnlist = []
    
    maxss = max(resulta,resultb,resultc)
    
  
    
    if resulta == maxss:
        returnlist.append(1)
    if resultb == maxss:
        returnlist.append(2)
    if resultc == maxss:
        returnlist.append(3)
        
    print("Result", returnlist)
        

    return returnlist