import re
import os

def filterNumbers():
    inputFileName = 'inputNumbers.txt'
    outputFilename = 'filteredNumbers.txt'
    currentDirectory = os.path.dirname(os.path.abspath(__file__))

    inputNumbersFile = os.path.join(currentDirectory, inputFileName)
    outputFilteredNumbersFile = os.path.join(currentDirectory, outputFilename)
    numbers = []

    # Read the numbers from the file
    with open(inputNumbersFile, "r") as file:
        for line in file:
            #replace everything except numbers with nothing
            line = re.sub(r'[^0-9]', '', line)
            if(len(line) == 10):
                numbers.append(line.strip())

    # Write the filtered numbers to a file
    with open(outputFilteredNumbersFile, "w") as file:
        #join each array element with , and \n
        array_str = '\n'.join(str(element) for element in numbers)

        file.write(array_str)

    # Delete the contents of the file
    with open(inputNumbersFile, "w") as file:
        file.truncate()