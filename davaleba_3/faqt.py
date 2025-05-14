def faqtoriali (one , ricxvi):
    namravli = 1
    for number in range(one, ricxvi+1):
        number1 = namravli
        namravli = number * number1
    return namravli


one = 1
ricxvi = int(input("შეიყვანეთ რიცხვი : "))




shedegi = faqtoriali (one, ricxvi)
print(f'{shedegi}')
