import vobject
import os

# Create a new vCard object
vcard = vobject.vCard()
contacts = []

# input file for phone numbers
filename = 'filteredNumbers.txt'
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filteredInputNumbersFile = os.path.join(currentDirectory, filename)
with open(filteredInputNumbersFile, "r") as file:
    filteredInputNumbersFileData = file.read()
phoneNumbers = filteredInputNumbersFileData.split("\n")


#vcard for each phone number
for index, value in enumerate(phoneNumbers):
# Set the contact information
    vcard = vobject.vCard()
    vcard.add('n')
    vcard.n.value = vobject.vcard.Name(family='Client'+str(index))
    vcard.add('fn')
    vcard.fn.value = 'Client'+str(index)
    vcard.add('tel')
    vcard.tel.value = value
    vcard.tel.type_param = 'CELL'
    contacts.append(vcard)

# Write the vCard to a file
filteredInputNumbersFile = '/Users/theshdb/Documents/Jaffer/Jaffer01/contact.vcf'  
with open(filteredInputNumbersFile, 'w') as file:
    for contact in contacts:
        file.write(contact.serialize())
print('vCard file created.')

input = input("Type Y to delete the filteredNumbers.txt file: ")
if input == 'Y':    
    # Delete the contents of the file
    with open(filteredInputNumbersFile, "w") as file:
        file.truncate()
    print('filteredNumbers.txt file data deleted.')