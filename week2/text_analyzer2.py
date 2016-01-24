user = list(input('Please enter a text string: ').lower())
vowaldict = {'a':0,'e':0,'i':0,'o':0,'u':0}
for x in user:
    if x in vowaldict:
        vowaldict[x] +=1
print(vowaldict)
