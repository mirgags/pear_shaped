import datetime
my_name = 'Mark Miraglia'
my_age = 34
my_height = 5 * 12 + 9
my_weight = 190
my_eyes = 'green'
my_teeth = 'yellow'
my_hair = 'black'
the_date = datetime.date.today()

print "Today is %s." % the_date
fix_date = "Not this weird pythony thing: %r." % the_date
print fix_date
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "That's not that heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "his teeth are usually %s depending on the cigarettes." % my_teeth

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
