import time
import sys

def add(a, b):  
    return a+b

def sub(a, b):  
    return a-b 

def mul(a, b):  
    return a*b 

def div(a, b):  
    return a//b

print("Simple Calculator!")
print("""Select operation:
1. Addition  
2. Subtraction
3. Multiply
4. Divide or '0' to exit.""")
        
def main():
    while True:
        choice = input("\nEnter your choice: ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if choice > 4:
            print("Please Input correct choice... Try Again!")
            continue

        elif choice == 0:
            print("Exiting...")
            time.sleep(2)
            sys.exit(1)

        elif choice == 1 or 2 or 3 or 4:
            try:
                a = int(input("Enter number 1: "))
                b = int(input("Enter number 2: "))

                if choice == 1:
                    print('~~', add(a, b), '~~')

                elif choice == 2:
                    print('~~', sub(a, b), '~~')

                elif choice == 3:
                    print('~~', mul(a, b), '~~')

                elif choice == 4:
                    print('~~', div(a, b), '~~')

            except ValueError:
                print("Error = Please type only numbers !")
        continue

main()








