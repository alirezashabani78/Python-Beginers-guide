"""""
This program will ask you to input a team name and the scores for your team and the other team 
 in 5 games ,and the result in 5 games will be calculated and printed out in wins draws or looses 
"""""
team_name = str (input("please enter your team name: "))
count = 1
win = 0
draw = 0
lose = 0
while count <=5:
    scored = int (input("goals scored in match# " + str (count)+ ":"))
    scored_against = int (input("goals scored_against in match# " + str (count)+ ":"))
    if scored > scored_against:
        win +=1
        count +=1
    elif scored == scored_against:
        draw  += 1
        count += 1
    elif scored < scored_against:
        lose += 1
        count += 1
print (team_name)
print("win " + str (win))
print("draw " + str  (draw))
print("lose " + str  (lose))
print("points" + str(int (win *3) + (draw *1)))
