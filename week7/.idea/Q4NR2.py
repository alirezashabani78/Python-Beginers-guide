while True:
    question = str(input("enter a string"))
    if "ni!" in question.lower():
        print("exit")
        break
    else:
        print("keep enter a string")