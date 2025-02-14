import sys

n = int(sys.stdin.readline())
room = 1
last_num = 1

while n > last_num:
    last_num += 6*room
    room += 1

print(room)
