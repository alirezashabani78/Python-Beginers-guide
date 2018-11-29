students = int (input("please enter the number of students: "))
if students >=1 and range <=23:

    print("error ur value of student is not valid")

    students = int (input("please enter then number of students"))
    number_of_pcs = int(input("please enter the number of pcs in the lab: "))
    if number_of_pcs <=5:
        print ("size of the lab is too small, enter a new lab size")
        pcs_in_the_lab = int(input("please enter the number of pcs in the lab"))
        labs_needed = number_of_pcs /students
        if labs_needed < 1:
            print ("you will need more than one lab")
            if labs_needed > 1:
                print("you will only need one lab")

