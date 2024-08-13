import sys

str=sys.stdin.readline().rstrip()
boom=sys.stdin.readline().rstrip()
boom_len=len(boom)
stack=[]

for i in range(len(str)):
    stack.append(str[i])
    if ''.join(stack[-boom_len:]) == boom:
        for _ in range(boom_len):
            stack.pop()
 
if(stack):
    print(''.join(stack))
else:
    print("FRULA")