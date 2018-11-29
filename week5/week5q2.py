"""""
This program will ask you to type the number of students and if the number are smaller then 1 it will be an 
error message and you will be asked to type a new number, The same will happen if you type a number of pcs 
smaller then 1, the program will calculate how many computer labs that will be needed.
"""""
___name___ = "Adam.Lundell"
___StudentID___ = "u1853373"
___Email___ = "u1853373@hud.ac.uk"
___date____ = "18/10/2018"
students = int (input("enter a number of students: "))
if students <= 0:
    print("Error enter a new number")
    students = int(input("enter a number of students: "))
pcs = int(input("enter a number of computers in the labs: "))
if pcs <= 0:
    print("If there no pcs it can be no classes , "
        "type another number greater than 0")
    pcs = int(input("please enter the number of computers in the labs: "))
if students % pcs == 0:
        print("Labs needed "+str (int (students / pcs)))
elif students % pcs > 0:
        print("Labs needed " + str(int(students / pcs)+1))
elif students / pcs <= 1:
        print("1 lab needed")

