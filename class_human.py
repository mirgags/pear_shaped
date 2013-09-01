class Human(object):

    def __init__(self):
        self.condition = 'Alone in the immensity.'

    def think(self):
        print "Therefore I am."

mark = Human()
mark.think()
print mark.condition
