import re

read_file_path = "/Users/theshdb/Documents/Jaffer/numbers.txt" 
write_file_path = "/Users/theshdb/Documents/Jaffer/clean_numbers.txt"
numbers = []

with open(read_file_path, "r") as file:
    for line in file:
        #replace everything except numbers with nothing
        line = re.sub(r'[^0-9]', '', line)
        if(len(line) == 10):
            numbers.append(line.strip())

with open(write_file_path, "w") as file:
    #join each array element with , and \n
    array_str = '\n'.join(str(element) for element in numbers)

    file.write(array_str)
