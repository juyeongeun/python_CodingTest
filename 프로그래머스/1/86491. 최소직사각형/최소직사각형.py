def solution(sizes):
    answer = 0
    row=[]
    col=[]
    
    for i in sizes:
        if i[0]>i[1]:
            row.append(i[0])
            col.append(i[1])
        else:
            row.append(i[1])
            col.append(i[0])
    
    max_row=sorted(row, reverse=True)
    max_col=sorted(col, reverse=True)
    
    
    answer=max_row[0]*max_col[0]
    
    return answer