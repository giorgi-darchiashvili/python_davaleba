def tabula (n):
    for i in range (1,11):
        yield f"{n} * {i} = {n * i}"


ricxvi = int(input("შეიყვანეთ რიცხვი : "))

for gam_tab in tabula(ricxvi):
    print (gam_tab)