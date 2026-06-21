e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    elif(i%2!=0):
      o_count=o_count+1
print("odd=",o_count)
print("even=",e_count)