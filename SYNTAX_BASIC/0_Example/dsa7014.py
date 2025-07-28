
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        st = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                st.append(int(s[i]))
            else:
                x = st.pop()
                y = st.pop()
                if s[i] == '+':
                    st.append(x + y)
                elif s[i] == '-':
                    st.append(x - y)
                elif s[i] == '*':
                    st.append(x * y)
                else:
                    st.append(x // y)
        print(st.pop())