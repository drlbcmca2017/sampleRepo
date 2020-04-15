#GUI Introduction
#need to import Tkinter module

from GUI import *


print("---> Welcome to GUI Introduction <---")
while(1):
	print "Select any one GUI to view"
	print "1.Spinbox \n2.Checkbutton \n3.Label & Textbox \n4.Button & MessageBox \n5.Radio Button\n"
	print "99. TO EXIT\n"
	ch=input("Your Option? ")
	if(ch==99):
		print "THANK YOU"
		break
	elif(ch==1):
		print "---> Spinbox\n\n"
		spinBox()
		
	elif(ch==2):
		print "---> Checkbutton\n\n"
		checkButton()

	elif(ch==3):
		print "---> Label & Textbox\n\n"
		label()

	elif(ch==4):
		print "---> Button & Message box\n\n"
		button_messagebox()

	elif(ch==5):
		print "---> Radio Button\n\n"
		radioButton()
	else:
		print "!! Wrong Option !!"
print "Bye...Bye.."
