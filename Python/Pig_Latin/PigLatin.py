#Program recieves a string prints the pig latin word for it

#Raw input removes the requirement of quotations around text input
text = raw_input('Enter a string: ')

#Slices the first letter and adds ay to it
pigText = text[1:] + "-" + text[0] + "ay"
print "The word is " + text + " the pig latin is " + pigText
