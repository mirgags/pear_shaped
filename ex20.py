from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def print_a_line(line_count, f):
    print line_count, f.readline(),

def rewind(f):
    f.seek(0)

current_file = open(input_file)

print "First print the whole file: \n"

print_all(current_file)

print "Noew go to the beginning"

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

