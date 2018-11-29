def nii_test(word, question):
    return word.lower() in question.lower()
    while True:

        question = str (input("enter a name of a string"))
        if "ni!" in question:
            print("exit")
            break
        else:
            print("keep give me strings")

