# Calculator

def addition ():
    print("Addition")
    n = input("Enter the number: ")
    t = 0 #Total number enter
    ans = 0
    while (n != '='):
        n = float(n)
        ans = ans + n
        t+=1
        n = input("Enter another number (= to calculate): ")
    return [ans,t]


def subtraction ():
    print("Subtraction");
    n = input("Enter the number: ")
    t = 0 #Total number enter
    ans=0
    while (n != '='):
        n = float(n)
        if (t==0):
            ans = n
        else:
            ans = ans - n
        t+=1
        n = input("Enter another number (= to calculate): ")
    return [ans,t]


def multiplication ():
    print("Multiplication")
    n = input("Enter the number: ")
    t = 0 #Total number enter
    ans = 1
    while (n != '='):
        n = float(n)
        ans = ans * n
        t+=1
        n = input("Enter another number (= to calculate): ")
    return [ans,t]

def division():
    print("Division")
    n = input("Enter the first number: ")
    n = int(n)
    m = input("Enter the second number: ")
    m = int(m)
    a = n//m
    b = n%m
    return [a,b]


def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]


# main...

while True:
    list = []

    print("Simple Calculator")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'd' for division")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")

    c = input(" ")

    if c != 'q':
        if c == 'a':
            list = addition()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == 'd':
            list = division()
            print("Quotient = ", list[0], " Remainder = ", list[1])
        elif c == 'v':
            list = average()
            print("Answer = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, Invilid character...Enter Again.")
    else:
        print("Thanks for using the calculator...Quitting!")
        break



