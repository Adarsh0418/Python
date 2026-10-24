num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
choice = input("Enter your choice  :Add-1, Sub- 2, Mul-3, div-4, Squareofnumber-5, floor-6, modules-7 :")
if choice == '1':
    print("Addition is: ", num1 + num2)
elif choice == '2':
    print("Subtraction is: ", num1 - num2)
elif choice == '3':
    print("Multiplication is: ", num1 * num2)
elif choice == '4':
    print("Divison is: ", num1 / num2)
elif choice == '5':
    print("Sqaure of number num1 is: ", num1 ** 2)
    print("Sqaure of number num2 is: ", num2 ** 2)
elif choice == '6':
    print("Floor is: ", num1 // num2)
elif choice == '7':
    print("Modules is: ", num1 % num2)
else:
    print("Invalid choice...")