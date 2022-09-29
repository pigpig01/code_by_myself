msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
opers = ["+", "-", "*", "/"]
def read_calc():
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    if x.isalpha() or y.isalpha():
        print(msg_1)
        return read_calc()
    else:
        if oper in opers:
            X = float(x)
            Y = float(y)
            if oper == opers[0]:
                result = X + Y
                print(result)
            if oper == opers[1]:
                result = X - Y
                print(result)
            if oper == opers[2]:
                result = X * Y
                print(result)
            if oper == opers[3] and Y != 0:
                result = X / Y
                print(result)
            elif oper == opers[3] and Y == 0:
                print(msg_3)
                return read_calc()

        else:
            print(msg_2)
            return read_calc()
read_calc()
