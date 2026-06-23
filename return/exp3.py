s_username="EMC"
s_password="123"

uname=input("enter user name :")
password=input("enter value for password:")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)