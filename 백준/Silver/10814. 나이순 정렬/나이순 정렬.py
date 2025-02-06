import sys

N = int(sys.stdin.readline())

people = []

for i in range(N):
    age, name = sys.stdin.readline().split(" ")
    people.append((int(age), i, name))

sorted_people = sorted(people, key=lambda x: (x[0], x[1]))

for age, _, name in sorted_people:
    print(age, name.rstrip())
