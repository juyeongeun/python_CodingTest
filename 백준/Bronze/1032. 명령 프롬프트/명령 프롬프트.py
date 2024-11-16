N = int(input())  # 파일의 개수 입력
arr = []  # 빈 리스트로 초기화

# 파일 이름 입력받아 리스트에 추가
for i in range(N):
    arr.append(input())

result = list(arr[0])  # 첫 번째 파일 이름을 리스트로 변환하여 초기 패턴으로 설정

# 나머지 파일 이름들과 비교하여 공통되지 않는 위치는 '?'로 대체
for i in range(1, N):
    for j in range(len(arr[0])):
        if arr[i][j] != result[j]:
            result[j] = '?'

# 결과를 문자열로 변환하여 출력
print(''.join(result))
