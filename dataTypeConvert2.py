#check for data type conversion

#list to tuple?

l1=[10,20,"list1"]
l2=["list2",30,40]
l3=[50,'list3',60]
t=(10,20.252,'tuple')
d={"k1":123,"k2":'Naming',"k3":'Class',"k4":25,"k5":'Vizag'}
def l_t():
	print "Lists ",l1,"   ",l2,"   ",l3
	tpl=(l1,l2,l3)
	print "tuple ",tpl

def t_l():
	list=[t,t,t]
	print "List with tuple values  ",list
def dic():
	print(d)
	print(d.keys())
	print(d.values())
