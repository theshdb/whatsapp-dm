import vobject

# Create a new vCard object
vcard = vobject.vCard()
contacts = []

#reading phone numbers
file_path = '/Users/theshdb/Documents/Jaffer/Jaffer01/clean_numbers.txt'

with open(file_path, "r") as file:
    file_content = file.read()

#array of phone numbers
phones = file_content.split("\n")

#vcard for each phone number
for index, value in enumerate(phones):
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
file_path = '/Users/theshdb/Documents/Jaffer/Jaffer01/contact.vcf'  
with open(file_path, 'w') as file:
    for contact in contacts:
        file.write(contact.serialize())
print('vCard file created.')
