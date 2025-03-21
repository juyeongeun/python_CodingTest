def solution(participant, completion):
    people = {}  
    
    for i in participant:
        if i in people:  
            people[i] += 1
        else:
            people[i] = 1
    
    for i in completion:
        people[i] -= 1
        
    for i in people:  
        if people[i] > 0:
            return i 
        
