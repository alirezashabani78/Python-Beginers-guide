liquor = input ("please enter the liquor shop\'s name ")

price_1 = int (input ("the first price ")[:-1])#the[:-1] removes the p when i write "10p 20p 30p" becouse it is -1 and
price_2 = int (input ("the second price ")[:-1])#removes 1 from the right so removes the "p" and its a int so it means that i
price_3 = int (input ("the third price ")[:-1])#-can only use numbers when i input the prices.
price_4 = int (input ("the fourth price ")[:-1])
price_5 = int (input ("the fifth price ")[:-1])
tuple = (price_1, price_2, price_3, price_4, price_5)#tuple = prices do so we can use the tuple to find out of the lowest/highest price

print (tuple) #it showes all the prices stored inside of the tuple.
total_price = price_1 + price_2 + price_3 + price_4 + price_5#shows that total price is all prices + eachother

print ("total price is " + str (total_price)+"")#prints out the total price
average_price = total_price /5 #so you can calculate the average price that is the total price /5

print ("average  price at " + liquor + " is " +str (average_price)+"P,")#prints out the average price
print("the lowest price at " + liquor + " is " +str(min(tuple))+"p,")#(min(tuple)) show you the smallest price
print("the highest price at " + liquor + " is " +str(max(tuple))+"p,") #(max(tuple))show you the max price
