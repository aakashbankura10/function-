# def nameofyourfunction ( varuable, constant,  attributes you want to pass in you function to take input and values)
# call functino :function name ( attributes)
def calculator (a, b, sign):
    if sign == "+":
        print(a + b)
    elif sign == "-":
        print(a - b)
    elif sign == "*":
        print(a * b)
    elif sign == "/":

        print(a / b)
    else :
        print("Invalid input")
sign = input("Enter sign: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
calculator(a, b, sign)
