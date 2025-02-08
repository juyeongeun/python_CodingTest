import sys

N = int(sys.stdin.readline().strip())
log = {}

for _ in range(N):
    name, state = sys.stdin.readline().strip().split()
    if state == "enter":
        log[name] = True
    else:
        if name in log:
            del log[name]

print("\n".join(sorted(log.keys(), reverse=True)))
