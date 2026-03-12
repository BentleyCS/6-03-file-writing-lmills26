import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    file = open(fileName, "w")
    for item in inputList:
        file.write(item + "\n")
    file.close()

def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    file = open(fileName, "r")
    names = file.readlines()
    file.close()

    names = [name.strip() for name in names if name.strip()]
    names.sort()

    file = open(targetFile, "w")
    for name in names:
        file.write(name + "\n")
    file.close()
sortNames("names.txt","namesNew.txt")


def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    file = open("scores. txt","a")
    file.write(str(newScore) + "\n")
    file.close()

    file = open("scores. txt", "r")
    scores = file.readlines()
    file.close()

    scores = [int(score.strip()) for score in scores if score.strip()]
    average = sum(scores) / len(scores)
    return average
print(highScore(random.randint(1,100)))

