def switchFileFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        fileToSwitch = fileToSwitch + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()