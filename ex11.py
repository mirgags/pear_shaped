age = int(raw_input("How old are you?"))
height = raw_input("How tall are you?")
weight = int(raw_input("How much you weigh?"))

print "So, you're %d years old, you are %s tall, and you're a fat bastard at %d pounds.  I guess it's better than %d pounds." % (age, height, weight, weight + 50)
