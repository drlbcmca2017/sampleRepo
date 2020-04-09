#Assign 3 
#print  1 to n number
#print 2,4,6,8,10,12,10,8,6,4,2
#print fibonacchi series : 1,1,2,3,5,8,13,21...144

def prntEvenSeries(n):
	i=2
	for i in range(2,n+1,2):
		if(i<=n):
			print(i)
	i=n
	for i in range(n+2,2,-2):
		if(i>1):
			print(i)
n=input("Enter a number :")
prntEvenSeries(n)

#completed	