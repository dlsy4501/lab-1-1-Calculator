# 간단한 계산기 코드의 일부
# ******** 함수 선언 ********
def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def 거듭제곱(x, y):
    return x ** y

def 몫(x, y):
    return x // y

def 나머지(x, y):
    return x % y

    
# ******** 몸체 ********

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.거듭제곱")
print("6.몫")
print("7.나머지")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7):")

num1 = float(input("첫번째 숫자를 입력하시오:"))
num2 = float(input("두번째 숫자를 입력하시오:"))

if choice == '1':
    print(num1, "+" ,num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-",num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*" ,num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/" ,num2,"=", divide(num1,num2))

elif choice == '5':
    print(num1, "**" ,num2,"=", 거듭제곱(num1,num2))

elif choice == '6':
    print(num1, "//" ,num2,"=", 몫(num1,num2))

elif choice == '7':
    print(num1, "%" ,num2,"=", 나머지(num1,num2))
    
else:
    print("틀린 입력을 하였습니다.")
