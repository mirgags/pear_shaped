from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copy %s to %s" % (from_file, to_file)

open(to_file, 'w').write(open(from_file).read()), open(to_file).close

#print "File is %d bytes" % len(indata)

#print "Does file exist yet? %r" % exists(to_file)
#print "Enter to continue"
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print "done"
#out_file.close()
#open(from_file).close()
