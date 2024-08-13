def main():
    math_interpreter()


def math_interpreter():
    x, y, z = input ("Expression: ").split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        print (f"{x+z:.1f}")
    elif y == "-":
        print (f"{x-z:.1f}")
    elif y == "*":
        print (f"{x*z:.1f}")
    elif y == "/":
        print (f"{x/z:.1f}")
    else:
        print ("not a valid expression")



main()

