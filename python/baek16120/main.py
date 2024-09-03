import sys


input = sys.stdin.readline

a = list(input())

st = list()


for i in a[:-1]:

    st.append(i)

    if i == "P" and len(st) >= 4 and st[-4:] == list("PPAP"):

        for j in range(4):
            st.pop()
        st.append("P")

if st == list("P"):
    print("PPAP")
else:
    print("NP")