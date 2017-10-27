userinput = str(raw_input('Enter a string:'))

def num_of_words(input):
    array = input.split()
    return len(array)

out = num_of_words(userinput)
print out