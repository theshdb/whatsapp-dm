file_path = '/Users/theshdb/Documents/Jaffer/clean_numbers.txt'

with open(file_path, "r") as file:
    file_content = file.read()

phones = file_content.split(",\n")

for phone in phones:
    print(phone)
    