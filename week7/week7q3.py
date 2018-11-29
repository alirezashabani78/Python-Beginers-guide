email = input(str("type a email adress "))
print (email [:-10])

def name(email):
    return email[:email.find("@")]