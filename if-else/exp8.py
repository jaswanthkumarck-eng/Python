salary=int(input())
age=int(input())
if(salary>=20000 or age<=25):
    loan=int(input())
    print("you are eligible for loan")
    if(loan>50000):
        print("loan eligible amount is 50000")
    else:
        print("loan eligible")
else:
    print("you are not eligible for loan")
    