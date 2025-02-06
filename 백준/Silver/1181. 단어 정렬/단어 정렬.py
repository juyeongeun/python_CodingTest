import sys

N = int(sys.stdin.readline())
word_list = set()
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.add((word, len(word)))


result = list(sorted(word_list, key=lambda x: (x[1], x[0])))

for word, _ in result:
    print(word)
