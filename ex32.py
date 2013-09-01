fruits = []

with open('fruitlist.txt', 'r') as fruitlist:
    for line in fruitlist:
        fruits.append(line.rstrip())

yeses = ['YES', 'OK', 'SURE', 'YEAH', 'OKAY', 'SI']
nos = ['NO', 'NOPE', 'NAH', 'UH-UH']

for fruit in fruits:
    answer = raw_input("Would you like some %s? (yes/no) > " % fruit).upper()
    for yes in yeses:
        if answer == yes:
            print "Here you go."

answer = raw_input("Is there any fruit you like that I didn't offer? > ")

while not answer.upper() in nos: 
    for yes in yeses:
        if answer.upper() == yes:
            fruits.append(raw_input("What is it? > "))
            answer = raw_input("Is there any fruit you like that I didn't offer? > ")
    if answer.upper() != "YES":
        answer = raw_input("I didn't get that, is there some other fruit you want? > ")

writefile = open('fruitlist.txt', 'w')

for fruit in fruits:
    writefile.write("%s\n" % fruit)
