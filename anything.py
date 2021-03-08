def countWords():
    fileName = input("Enter The File Name:")
    numberOfWords = 0
    file = open(fileName, "r")
    for i in file:
        words = i.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:" + str(numberOfWords))
countWords()