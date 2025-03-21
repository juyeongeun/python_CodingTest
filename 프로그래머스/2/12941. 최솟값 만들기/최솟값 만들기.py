def solution(A,B):
    answer = 0
    sort_A=sorted(A)
    sort_B=sorted(B)
    for i in range(len(A)):
        answer+=(sort_A[i]*sort_B[len(A)-i-1])
        
    return answer