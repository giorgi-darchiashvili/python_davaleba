def diapazoni ():
    for number in range(num1,num2+1):
        if number % 2 == 0:
            print(f"{number}")


num1 = int(input("number one : "))

num2 = int(input("number two : "))

diapazoni()