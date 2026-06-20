score=int(input("Enter your score: "))
if(score<35):
    print("poor student")
elif(score >35 and score <70):
    print("avg student")
elif(score<70 and score >100):
    print("good student")
else:
    if (score>100):
        print("invalid input")
     



