"""""
This program will let a user input his own number of pupils and sweets and calculate how many each pupil will 
have and the leftover to the teacher.
"""""
pupils = int (input ("pupils = "))
sweets = int (input ("sweets = "))

print ("each student get: "+str(int (sweets / pupils))+" sweets each")
print ("leftover is: "+str(int (sweets % pupils ))+" sweets")





