#getting number
def getNumber():
    """
    This function gets an input from the user.It checks if the input
    includes only values (0,1,2,3,4,5,6,7,8,9). If it includes any other
    include it is empty the use is again prompted to enter the number.
    It returns a integer
    """
    num1 = ""
    key = 'a'
    while key != 'q':
        while num1 == "":
            num = input('\tEnter a number: ')
            for i in range(len(num)):    
                if ord(num[i]) >= 48 and ord(num[i]) <= 57:
                    num1 += num[i]
                else:
                    num1 = ""            
                    break
            key = 'q'    
    return int(num1)

#Althematic operations
def mathOperation(num1, num2):
    """
    This method takes in two numbers.
    It gets an arthematic operator from the user
    Prints the results of the mathematical operation in a mathematic
    statement
    """
    op = input("\tEnter operator(*,/,-,+): ")

    print("\n....................RESULT........................")

    match op:
        case '+':        
            print(f"\t{num1} {op} {num2} = {num1 + num2}") 
        case '-':        
            print(f"\t{num1} {op} {num2} = {num1 - num2}")    
        case '/':        
            print(f"\t{num1} {op} {num2} = {num1 / num2}")    
        case '*':        
            print(f"\t{num1} {op} {num2} = {num1 * num2}")    
        case _:
            print("\tInvallid operator")
    print("....................RESULT........................")


#menu
def menu():
    """
    Thiis method prints a menu with options from which the user can
    select the next action
    """
    print("\n\t==========MENU===========")
    print("\t1. Change values")
    print("\t2. Change operator(*,/,-,+)")
    print("\t3. Exit")
    print("\t==========================")

def main():
    """
    This is the method where all the other method are called from.
    """
    print("=====================MY CALCULATOR=====================")
    print("*******************************************************")
    num1 = getNumber()
    num2 = getNumber()
    mathOperation(num1, num2)

    key = 'a'
    while key != 'q':
        menu()
        opt = int(input("\n\tChoose a number from the menu: "))
        while opt != 3:
            match opt:
                case 1:
                    #number 1
                    num1 = getNumber()
                    num2 = getNumber()
                    mathOperation(num1, num2)
                    menu()
                    opt = int(input("\t\nChoose a number from the menu: "))
                case 2:
                    mathOperation(num1,num2)
                    menu()
                    opt = int(input("\t\nChoose a number from the menu: "))
                case 3:
                    print("Thank for using Sempoz Calc")
                    
                case _:
                    print("Invalid input")
        print("\n***************Thank you for using Sempoz Calc***************")
        key = 'q'

main()
