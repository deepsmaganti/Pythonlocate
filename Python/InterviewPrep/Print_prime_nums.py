num = int(raw_input('Enter the number: '))

for j in range(2,num):
    prime = True
    for i in range(2,j):
        if (j%i==0):
            prime = False
            break
    if prime:
       print j