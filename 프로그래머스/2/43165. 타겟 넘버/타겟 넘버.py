def solution(numbers, target):
    sum = [0]          
    count = 0 

    for num in numbers : 
        temp = []
	
        for leaf in sum : 
            temp.append(leaf + num)
            temp.append(leaf - num)

        sum = temp 

    for leaf in sum : 
        if leaf == target : 
            count += 1
            
    return count