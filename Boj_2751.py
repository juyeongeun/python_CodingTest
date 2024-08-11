import sys

N = int(input())
arr = list(map(int, sys.stdin.read().split()))  # 빠르게 입력받아 리스트로 변환

arr.sort()  # 오름차순으로 정렬

for i in range(N):
    print(arr[i])
