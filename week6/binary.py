"""""
This program will print out 0-128 in 8 bit binary numbers from 00000000 to 01111111
"""""
for number in range (128):
    print (number, "{0:08b}".format(number))
