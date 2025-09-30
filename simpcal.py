num1 = float(input("Enter a First Number:"))
num2 = float(input("Enter a Second Number:"))

print("\n Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice(1/2/3/4): ")

if choice =='1' or choice=='+':
    result=num1+num2
    print(f"\n Result: {num1} + {num2} = {result}")

elif choice =='2' or choice=='-':
    result=num1-num2
    print(f"\n Result: {num1} - {num2} = {result}")

elif choice =='3' or choice=='*':
    result=num1+num2
    print(f"\n Result: {num1} X  {num2} = {result}")


elif choice =='4' or choice=='/':
    if num2 != 0:
        result = num1 / num2
        print(f"\n Result: {num1} / {num2} = {result}")
    else:
        print("\n Error: Division by zero is not allowed!")
else:
    print("\n Invalid choice! Please select a valid operation.") 