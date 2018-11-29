"""""
This program will ask you to input a username ,id number and a password, if you type 
huddersfield, justinbieber ,cheese,canalside , your username or the id_number the program will give an errormessage 
and ask you to type a new password. if the password is valid it will ask you to retype the password.
"""""
username = str (input("please enter your username: "))
id = str (input("please enter your id number: "))
wrong = ("huddersfield", "justinbieber", "cheese", "canalside", username, id)
password = str (input("enter password: "))
if password in wrong:
    print ("error , password not valid")
else:
    reentered = str (input("enter password one more time "))
    if reentered == password:
        print("you entered a valid password")
    else:
        print("Error you did not re-enter the same password, shutdown")