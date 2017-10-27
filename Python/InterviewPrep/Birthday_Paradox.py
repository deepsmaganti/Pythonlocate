userinput = int(raw_input('Enter the number of people: '))

def bday_paradox(n):
    prob_w_diff_bday = 1
    for i in range(n):
        prob_w_diff_bday = (365-i) * prob_w_diff_bday
    total_prob = 365**n
    prob_same_bday = 1 - (float(prob_w_diff_bday)/total_prob)
    return prob_same_bday*100

out = str(bday_paradox(userinput))
print out+'%'