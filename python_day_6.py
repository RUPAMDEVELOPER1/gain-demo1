#Create and make functions for registration page and login page. Both pages should have both register and login
#button for their respective actions and the other button should redirect the user to new UI page. 
from PyQt5 import QtWidgets, uic
import sys
uname ='root'
upass ='password'
def open_second_ui():
    first.close()
    second.show()

    
def open_first_ui():
    second.close()
    first.show()
    
def validate_login():
    global uname, upass
    username=first.Uname.text()
    password=first.Upass.text()
    if username==uname and password==upass:
        first.Status_box.setText("Logged In")
    else:
        first.Status_box.setText("Try to Login Again")
        
def register_user():
    global uname, upass
    second.RegisterUsr.setText("Registration Done")
    uname=second.new_usr.text()
    upass=second.new_pass.text()
    

demo = QtWidgets.QApplication([])

second = uic.loadUi("/Users/smadhwal/Desktop/register.ui")   
first = uic.loadUi("/Users/smadhwal/Desktop/login.ui")

first.show()

# Assuming registerbtn is a QLabel
first.registerbtn.clicked.connect(open_second_ui)
second.LoginBtn.clicked.connect(open_first_ui)
first.loginbtn.clicked.connect(validate_login)
second.RegisterBtn.clicked.connect(register_user)

sys.exit(demo.exec_())
