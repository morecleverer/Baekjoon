def cantor(txt):
    if len(txt) == 1:
        return "-"

    else:
        a = str(cantor(txt[:len(txt) // 3]))
        b = str("".ljust(len(txt) // 3, " "))
        c= str(cantor(txt[2 * len(txt) // 3:]))
        return a+b+c


while True:
    try:
        n = input()
        if n == "":
            break
        else:
            n = int(n)
            text = "".ljust(3**n,"-")

            print(cantor(text))
    except EOFError:
        break