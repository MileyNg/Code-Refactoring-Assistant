import sys
for s in sys.stdin.readlines():
    st = []
    for c in s.strip().split():
        if c=='+':
            st.append(st.pop()+st.pop())
        elif c=='-':
            st.append(-st.pop()+st.pop())
        elif c=='*':
            st.append(st.pop()*st.pop())
        elif c=='/':
            st.append(1/st.pop()*st.pop())
        else:
            st.append(float(c))
    print st.pop()