def passorfail(score):
    if(score>35):
        print("pass")
    elif(score==35):
        print("just pass")
    else:
        print("fail")

score=int(input("enter your score :"))
passorfail(score)