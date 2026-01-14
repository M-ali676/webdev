print("******Multiple App Player******")
select=int(input("Select An App You Want To Work: \1. Calculator: \n2. Studemt Marksheet: \n3.Student ID Card: \n4.Student "))

if select==1:
    name=input("Enter Your Name")
    num1=eval(input("Enter num1 To proceed"))
    num2=eval(input("Enter num2 To proceed"))
    method=input("What you w1ant to do?: \n1.Addition \n2.Subtraction \n3.Division \n4. Multiply")
    if method=="1":
        print(f"This is your adddition: {num1+num2}")
    elif method=="2":
        print(f"This is your Subtraction:{num1-num2}")
    else:
        print("Invalid Inpput")
    
else:
    print("Invalid Input")


#Nested Decision in python
#multi - decision program!
# print("*****Welcome to netflix *****")
# name=input("Enter your name:")
# email=input("EnterYour Email:")
# password=input("Enter your password:")
# eage=int(input("Enter your age:"))
# if eage>=18:
#     print(f"Dear {name}, Welcome to Netflix!")
#     if email=="alisolangi676@gmail.com" and password=="Admin123":
#         print(f"Dear {name}, Welcome to the Netflix Sessions, Please select Category")
#     elif email=="imransolangi098@gmail.com" and password=="Admin098":
#         print(f"Dear {name}, Welcome to the Netflix Sessions, Please select Category")
#     elif email=="nomansolangi078@gmail.com" and password=="Admin078":
#         print(f"Dear {name}, Welcome to the Netflix Sessions, Please select Category")
#     elif email=="imransolangi098@gmail.com" and password=="Admin098":
#         print(f"Dear {name}, Welcome to the Netflix Sessions, Please select Category")
#     elif email=="yousafsolangi098@gmail.com" and password=="Admin698":
#         print(f"Dear {name}, Welcome to the Netflix Sessions, Please select Category")
#     else:
#         print(f"Dear {name}, Your login Credentials are invalid!")
# else:
#     print(f"Dear {name}, Please watch pogo!")

print("************Multiple App Player **************")

select=int(input("Select an App you want to work: \n1. Calculator \n2. Student Marksheet \n3. Clothing Store \n4. Car Recomendation "))
if select==1:
	method=input("what your want to do?: \n1. Additon \n2. subtraction \n3. Division \n4. Multiply")
	name=input("Enter Your name:")
	num2=eval(input("Enter  to proceed"))
	if method=="1":
		print(f"This is your Addition: {num1+num2}")
	elif method=="2":
		print(f"This is your Addition: {num1-num2}")
	else:
		print("invalid input!")
else:
	print("Invalid input!")
	
	



