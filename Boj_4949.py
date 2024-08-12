while True:
    a = input()
    if a == ".":
        break
    
    stack = []
    is_balanced = True

    for i in a:
        if i in "([":  # if i == '(' or i == '[': 동일
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] != "(":
                is_balanced = False
                break
            stack.pop()
        elif i == "]":
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
