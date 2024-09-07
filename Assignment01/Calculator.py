print("Welcome to the Simple Calculator!")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

def sum(a,b):
    return(a+b)
def difference(a,b):
    return(a-b)
def product(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

while True:
    print("Select an operation")
    print("1. Addition") 
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    option = input("Enter the operation number 1/2/3/4")
    if option == "1":
        print("Result:", a,"+",b,"=",sum(a,b))
    elif option == "2":
        print("Result:",a,"-",b,"=",difference(a,b))
    elif option == "3":
        print("Result:",a,"*",b,"=",product(a,b))
    elif option == "4":
        print("Result:",a,"/",b,"=",divide(a,b))
    else:
        print("Invalid result")

    calculation = input("Do you want to perform another calculation? (yes/no)")
    if calculation == "no":
        print("Goodbye")
        break
            
             

    