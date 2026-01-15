# Nested decision in Python

# print("****Exam Eligibility Program****")
# 
# name=input("Enter your name")
# email=input("Enter your email")
# totalclasses=int(input("Total classes"))
# attendend=int(input("Classes attendend"))
# medical=input("Medical certificate (yes/no):")
# 
# attendence_percentage=(attendend / totalclasses)*100
# if attendence_percentage >=75:
# 	print("Allowed to sit in exam")
# 	if medical =="yes":
# 		print("Allowed due to medical certificate(Special Permision)")
# 	else:
# 		print("Not Allowed to sit in exam!")
# else:
# 	print(f"Dear{name},Allowed in Exam/ Classes/except medical certificate, {email}:")
# 	


print("****Electricty Bill Program****")
name=input("Enter Your Full Name")
email=input("Enter Your Email")
units=int(input("Units Consumed:"))
customer=input("Customer type (domestic/comercial)").lower()

if customer=="domestic":
	rate=5
elif customer=="comercial":
	rate=8
	print("Invalid customer type")
	rate=0
	bill = units*rate
	if units>300:
		bill=bill+500
		print("Final Bill=",bill)
else:
	print("Tex apply for Government of Pakistan")


