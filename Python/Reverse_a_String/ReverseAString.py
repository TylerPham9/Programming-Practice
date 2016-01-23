#Program recieves a string and prints out the reverse of it

def reverse(txt):
    if len(txt) <= 1:
        return txt
    return reverse(txt[1:]) + txt[0]

#Raw input removes the requirement of quotations around text input
text = raw_input('Enter a string: ')

#String slicing [begin:end:step]
#runs through the string, stepping backwards
textRSlice = text[::-1]
print "The reverse of " + text + " is " + textRSlice

#Recursively reverse the text
textRRec = reverse(text)
print "The reverse of " + text + " is " + textRRec
