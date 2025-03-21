import sys

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

if __name__=="__main__":
    s=sys.stdin.readlin()