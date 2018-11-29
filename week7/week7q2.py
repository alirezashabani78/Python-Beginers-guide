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

if __name__ == '__main__':

    email = input(str("type a email adress "))
    print(email_address(email, "pop.ac.uk"))

    print (name_part (email))


"""if __name__ == '__main__':
        print(email_address(email, "pop.ac.uk"))
"""