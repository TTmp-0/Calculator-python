a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    print("Результат:", a + b)

elif operation == "-":
    print("Результат:", a - b)

elif operation == "*":
    print("Результат:", a * b)

elif operation == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print("Результат:", a / b)

else:
    print("Неизвестная операция")