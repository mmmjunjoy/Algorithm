import sys

input = sys.stdin.readline



# a,b,c = map(int, input().split())

# middle = []
# middle.append(a)
# middle.append(b)
# middle.append(c)

# #1
# maxs = max(middle)
# middle.remove(maxs)
# #2
# maxss = max(middle)
# middle.remove(maxss)
# #3
# maxsss  = middle[0]


while True:
    a,b,c = map(int, input().split())
    if a == b == c == 0:
        break

    
    list = [ a,b,c]
    
    if  sum(list) <= max(list)*2:
        print("Invalid")
    elif a == b == c :
        print("Equilateral ")
    elif a == b or b ==c or c ==a :
        print("Isosceles ")
    else:
        print("Scalene ")



    # else:

    #     if maxs >= maxss + maxsss :
    #         print("Invalid")




    #     else:
    #         if maxs == maxss == maxsss:
    #             print("Equilateral ")
    #         elif maxs == maxss or maxss == maxss  or maxsss == maxs:
    #             print("Isosceles ")
    #         else :
    #             print("Scalene ")
