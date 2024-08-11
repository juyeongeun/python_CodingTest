n=int(input())
score = list(map(int, input().split()))
max_num = max(score)

average = sum(score)
average = (average/max_num*100)/n

print(average)