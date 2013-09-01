def range_rolled(*args):
    if len(args) < 3:
        if len(args) == 1:
            start = 0
            end = args[0]
        elif len(args) == 2:
            start, end = args
        starterror = True
        enderror = True
        while True:
            try:
                start = int(start)
                starterror = False
                break
            except ValueError:
                print "arg1 is not an integer"
                starterror = True
                break
        while True:
            try:
                end = int(end)
                enderror = False
                break
            except ValueError:
                print "arg2 is not an integer"
                enderror = True
                break    
        if (starterror or enderror) != True:
            if start <= end:
                list = []
                while start <= end:
                    list.append(start)
                    start += 1
                return list
            else:
                print "arg1 must be less than or equal to arg2"
    else:
        print "function accepts only 1 or 2 arguments"

