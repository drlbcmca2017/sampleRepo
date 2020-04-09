#Assign 3 
#print  1 to n number
#print 2,4,6,8,10,12,10,8,6,4,2
#print fibonacchi series : 1,1,2,3,5,8,13,21...144

def prntFibo(n):
	i=j=1
	print(i)
	print(j)
	k=i+j
	while(k<=n):
		print(k)
		i=j
		j=k
		k=i+j	
print("\t<---Fibonacchi Series--->")
n=input("Enter UPTO number of Fibonacchi :")
prntFibo(n)


#completed