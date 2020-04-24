a=raw_input("enter maths_operator:")
if (a=="+"):
	b=input("enter 1st number")
	c=input("enter 2nd number")
	print("the sum is :"+str(b+c))
elif (a=="-"):
	b=input("enter 1st number")
	c=input("enter 2nd number")
	print("the difference is :"+str(b-c))
elif (a=="*"):
	b=input("enter 1st number")
	c=input("enter 2nd number")
	print("the multiplication is :"+str(b*c))	
elif (a=="/"):
	b=input("enter 1st number")
	c=input("enter 2nd number")
	print("the division is :"+str(b/c))
else:
	print("invalid!!")
	