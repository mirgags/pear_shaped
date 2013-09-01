# An interactive script that prompts the user to accept or reject fruit
# offerings and then asks if they want any other fruit that wasn't offered.
# Responses are stored in the fruitlist.txt file for later reading.


yeses = ['YES', 'OK', 'SURE', 'YEAH', 'OKAY', 'SI']
nos = ['NO', 'NOPE', 'NAH', 'UH-UH']
fruits = []

# imports list of fruits fro text file
with open('fruitlist.txt', 'r') as fruitlist:
    for line in fruitlist:
        fruits.append(line.rstrip())

# checks response input against list of approved responses.
def wants_fruit(answer, yeses, nos):
    more_fruit = ""
    for yes in yeses:
        if answer.upper() == yes:
            more_fruit = 'yes_fruit'
    for no in nos:
        if answer.upper() == no:
            more_fruit = 'no_fruit'
    if not (more_fruit == 'yes_fruit' or more_fruit =='no_fruit'):
        more_fruit = wants_fruit(raw_input("I'm sorry I didn't catch that, do you want some other fruit? > "), yeses, nos)
    return more_fruit

# adds requested fruit to list
def add_fruit(fruits):
    fruits.append(raw_input("What is it? > "))
    print "Oh ok, I'll bring some %s next time." % fruits[(len(fruits) - 1)]
    return fruits

# beginning of interactivw program
for fruit in fruits:
    answer = raw_input("Would you like some %s? (yes/no) > " % fruit).upper()
    for yes in yeses:
        if answer == yes:
            print "Here you go."

answer = raw_input("Is there any fruit you like that I didn't offer? > ")
more_fruit = "" 

while more_fruit != 'no_fruit':
    more_fruit = wants_fruit(answer, yeses, nos)
    if more_fruit == 'yes_fruit':
        fruits = add_fruit(fruits)
        more_fruit = ""
        answer = raw_input("Is there any fruit you like that I didn't offer? > ")

# opens and writes list to text file
writefile = open('fruitlist.txt', 'w')

for fruit in fruits:
    writefile.write("%s\n" % fruit)

