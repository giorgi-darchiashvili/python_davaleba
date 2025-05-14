num1 = int(input("პირველი რიცხვი : "))

num2 = int(input("მეორე რიცხვი : "))

moq = input("მოქმედება : ")

if moq == "+":
    calc = num1 + num2
elif moq == "-":
    calc = num1 - num2
elif moq == "*":
    calc = num1 * num2
elif moq == "/":
    calc = num1 / num2

print(calc)