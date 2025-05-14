def diapazoni (sacyisi, saboloo):
    for number in range(sacyisi,saboloo+1):
        if number % 2 == 0:
            print(f"{number}")


num1 = int(input("number one : "))

num2 = int(input("number two : "))

diapazoni(num1,num2)