def solution(nums):
    
    lens = len(nums) // 2
    
    hashdict ={}
    for num in nums:
        hashdict[hash(num)] = num
        
    
    result = 0
    if lens < len(hashdict):
        result = lens
    else:
        result = len(hashdict)
    

    
    answer = 0
    return result