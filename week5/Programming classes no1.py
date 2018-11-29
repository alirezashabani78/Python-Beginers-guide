"""""
This program will ask you to type the number of students and if the number are smaller then 1 it will be an 
error message and you will be asked to type a new number, The same will happen if you type a number of pcs 
smaller then 1, the program will calculate how many computer labs that will be needed.
"""""
while True:
    students = int (input("please enter the number of students: "))
    if students <= 0:

        print ("Error please enter a value that is more than 0")
    else:
        while True:

            pcs = int(input("please enter the number of computers in the labs: "))
            if pcs <= 0:
                print("If there no pcs it can be no classes , "
                      "type another number greater than 0")

            else:
                if students / pcs  <= 1:
                    print("1 lab needed")
                    break
                elif students % pcs == 0:

                    print("Labs needed "+str (int (students / pcs)))
                    break
                elif students % pcs > 0:
                    print("Labs needed " + str(int(students / pcs)+1))
                    break

        break









