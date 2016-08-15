def sentence(word):
    num_upper=0
    num_lower=0
    
    for x in word:
        if x.isupper():
            num_upper+=1
        elif x.islower():
            num_lower+=1
        else:
            pass
    print("UpperCase letters in the given sentence are:"+str(num_upper))
    print("LowerCase letters in the given sentence are:"+str(num_lower))

sentence(input("Enter a sentence to calculate the number of UpperCase & LowerCase letters in it: \n"))
