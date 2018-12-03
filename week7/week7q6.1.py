import random
def email_address (email, domain):
    if email.count ("@") != 1:
       return False
    if email[0] == "@":
        return False
    if email [(email.find ("@") +1) :] != domain:
        return False
    return True
def name_part (email):
    return email [:(email.find ("@"))]
def random_string(a):
    return random.choice(a)
def check(question):
    if question.lower().capitalize() == "Goodbye":
        return True
def random_string_1(b):
    return random.choice(b)
def str_in_str(word, question):
    return word.lower() in question.lower()
def random_shutdown():
    num =random.randint(0,101)
    if num < 15:
        return True
email = input(str("type a email adress "))
domain = "pop.ac.uk"
if email_address(email, domain) is True:
    print ("Welcome " +(email [:-10]))
    a = ["joe", "Gary", "Steven", "Tony", "Adam", "Linda"]
    print("Hello, my name is " + random_string(a) + ". i would be helping you today")
    count = 1
    while True:
        question = str(input("hello " + name_part(email) + "," " how can i help you? "))
        if "goodbye" in question.lower():
            print("exit")
            break
        if random_shutdown():
            print("connection lost,")
            break
        elif "library" in question.lower():
            print("Sorry the library is closed today")
        elif "i need coffee" in question.lower():
            print("yes you doo")
        elif "wifi" in question.lower():
            print("wifi connection is great across campus")
        elif "deadline" in question.lower():
            print("Sorry, your deadline has been extended 2 working days")
        elif question:
            b = ["Yes", "No", "Sounds interesting, tell me more", "haha! wow that was sick! tell me more", "maybe"]
            print("" + random_string_1(b) + "")
        else:
            print("Error")









