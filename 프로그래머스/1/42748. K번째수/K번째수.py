def solution(array, commands):
    resultlist=[]
    for i in range(len(commands)):
        a = commands[i][0] -1
        b = commands[i][1] 
        c = commands[i][2] 
        
        newlist = []
      
        for i in range(a,b):
            newlist.append(array[i])
            newlist.sort()
     
        result = newlist[c-1]
        resultlist.append(result)
            
      
#         print("new",newlist)

#         print("result", resultlist)
            
        

    return resultlist