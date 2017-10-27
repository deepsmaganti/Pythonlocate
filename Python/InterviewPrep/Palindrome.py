userinput = str(raw_input('Enter a string: '))

def palindrome_short(s):
    length = len(s)
    for i in xrange(0,length/2):
        if s[i] != s[(length-1)-i]:
            return False
    return True

def palindrome_reverse(s):
    return s == s[::-1]

out = palindrome_short(userinput)
out1 = palindrome_reverse(userinput)
print (out)
print (out1)