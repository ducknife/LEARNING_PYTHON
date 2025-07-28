
if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        s = input()
        st = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                st.append(str(s[i]))
            else:
                x = st.pop()
                y = st.pop()
                st.append(x + y + str(s[i]))
        print(st[0])

