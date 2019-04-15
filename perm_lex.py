def perm_gen_lex(a):
    """creates a list of all the perumations of a given string"""
    new = []
    new_str = ''
    for i in range(len(a)): # gets the index of each letter in the word
        new_str = a[:i] + a[i + 1:] #gets rid of indexed letter in the word
        Nlist = perm_gen_lex(new_str) #perm gens this new word
        if len(a) == 1 and len(new_str) == 0: #when there is only a one letter word it adds space so that the for loop will detect it
           Nlist.append(" ")
        for j in range(len(Nlist)):
            new.append(a[i] + Nlist[j]) #creates list of words
    for i in range(len(new)):# removes spaces added
        new[i] = new[i].strip()
    return new
 
