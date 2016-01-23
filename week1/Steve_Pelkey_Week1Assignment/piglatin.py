fullname = input("Please enter your name: ")
names = fullname.split(' ')
pignames=['Ellohay']
for n in names:
	pignames.append(n[1:].title()+ n[0] + 'ay')
putaspaceinit = " "
output = putaspaceinit.join(pignames)
print(output)
