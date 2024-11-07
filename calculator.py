print("Welcome to basic calculator project!")

n1=float(input("Enter the first number:"))
operation=input("Enter the operation like [+, -, *, /]:")
n2=float(input("Enter the second number:"))


if operation == "+":
    result=n1+n2
    print(f"The result:{result}")

elif operation == "-":
    result=n1-n2
    print(f"The result:{result}")

elif operation == "*":
    result=n1*n2
    print(f"The result:{result}")

elif operation == "/":
    result=n1/n2
    print(f"The result:{result}")

else:
    print("Invalid input")



