userinput = str(raw_input('Enter a string: '))

def Load_HashMap(input):
    array = input.split()
    new_array = {}
    for i in array:
        if i.lower() in new_array.keys():
            new_array[i.lower()] = new_array[i.lower()] + 1
        else:
            new_array[i.lower()] = 1
    # for key, value in new_array.items():
    #     if value == max(new_array.values()):
    #         return new_array , key
    print (new_array)
    for key, value in new_array.items():
        if value == 1:
            print (key)

Load_HashMap(userinput)