print("Welcome to PopChat. The University of Poppleton's Online Chat")

def email_address (email, domain):
    domain=email [email.find ("@") +1:]


    if email.count ('@') != 1:
       return False

    if email[0] == '@':
        return False

    if "." not in domain:
        return False

    if __name__ == '__main__':
        return False
    else:

        return True

email = input(str("To login , please type a valid email address "))
print(email_address(email, "pop.ac.uk"))





