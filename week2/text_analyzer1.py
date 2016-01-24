user = list(input('Please enter a text string: '))
vowals = set('aeiouAEIOU')
vowalcount = 0
iteration = 0
for x in user:
    iteration += 1
    if x in vowals:
        vowalcount += 1
        if vowalcount == 1:
            firstvowal = x
            nextchar = user[iteration]
if vowalcount == 0:
    print ("You have to enter at least one vowal")
    import os
    os._exit(1)
print("vowals:", vowalcount)
print("first vowel:", firstvowal)
print("character immediately after first vowel:", nextchar)

