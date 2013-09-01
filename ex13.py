from sys import argv

script, user_name = argv
prompt = '~~^~~ '

print "Hey pally I'm %s, is %s your handle?" % (script, user_name)
print "Why dont you make a superhero name at this cool prompt"
fourth = raw_input(prompt)
print "Ok %s, your superhero name is: %s " % (user_name, fourth)
