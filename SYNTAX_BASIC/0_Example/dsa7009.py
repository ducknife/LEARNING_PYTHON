
if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        s = input()
        stack = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                stack.append(str(s[i]))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append("(" + x + str(s[i]) + y + ")")
        print(stack[0])
