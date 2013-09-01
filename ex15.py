from sys import argv

script, filename = argv

txt = open(filename)

print "Here's the file %r:" % filename

print txt.read()

print "Now replace that text: "
new_txt = raw_input('> ')

txt.close()
txt = open(filename, 'a')
txt.write("\n%s\n" % new_txt)
print "Now let's add one more line:"
new_txt = raw_input('> ')
txt.write(new_txt)
txt.close()

txt = open(filename)
print txt.read()
