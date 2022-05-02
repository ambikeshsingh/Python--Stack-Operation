l=[]

while True:
    c=int(input("""
    1 Push Element
    2 pop Element
    3 Peek Element
    4 Display Stack
    5 Exit
    """))

    if c==1:
        n=int(input("Enter the Value"))
        l.append((n))
        print(l)


    elif c==2:
        if len(l)==0:
            print('Empty Stack')
        else:
            p=l.pop()
            print(p)
            print(l.pop())

    elif c==3:
        if len(l)==0:
            print("Empty stack")

        else:
            print("Peek Element" +l[-1])

    elif c==4:
        print("Display", l)

    elif c==5:
        break

    else:
        print("Invalid Option")






