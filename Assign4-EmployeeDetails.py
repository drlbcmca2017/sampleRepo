#Assign-4 : Accept the details of 5 Emps with 
#name, age, salary and print the details of Emp
#Find out total Salary provided to all Emp

class Emp5:
	empDB={}
	TotalSal=00.00
	#def __init__(self,name,age,salary):
		#empDic["name","age","salary"]={self.name,self.age,self.salary}
	
	def getInfo(self,n):
		#empDB={}
		#TotalSal=00.00
		count=0
		while(count!=n):
			print "Enter no.",count+1," Employee details:"
			name=raw_input("Name? ")
			age=input("Age? ")
			sal=input("Salary? ")
			empDic={"Emp_Name":name,"Emp_Age":age,"Emp_Salary":sal}
			note="EMP"+str(count)
			self.empDB[note]=empDic  #dictionary
			count=count+1
			self.TotalSal+=sal
	def showInfo(self):
		print ("---> Employee Database <--- ")
		for i in self.empDB.keys():
			print self.empDB[i]

e=Emp5()
print "---> Welcome to Employee details Entry <---"
n=input("Enter no. of employees : ")
e.getInfo(n)
e.showInfo()
print "Total Salary Paid is : ",e.TotalSal

#completed