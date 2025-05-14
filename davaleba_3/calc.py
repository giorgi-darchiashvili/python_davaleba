def calc (num1, moq, num2,):
    if moq == '+':
        return num1 + num2
    elif moq == "-":
        return num1 - num2
    elif moq == "*":
        return num1 * num2
    elif moq == "/":
        return num1 / num2
    else:
        print ("არასწორი მოქმედება")




n1 = int(input("შეიყვანეთ პირველი რიცხვი : "))
mo = input("შეიყვანეთ მოქმედება : ")
n2 = int(input("შეიყვანეთ მეორე რიცხვი : "))

print(calc(n1, mo, n2,))