class Human(object):

    def __init__(self, name):
        self.condition = 'Alone in the immensity.'
        self.name = name


    def think(self):
        print "Therefore I am."


class Poem(object):


    def __init__(self, lyrics, genre):
        self.lyrics = lyrics
        self.genre = "The poem is considered: %s." % genre


    def poetry(self):
        for line in self.lyrics:
            print line


alfred_prufrock = {'lyrics': ["In the room the women come and go,",
                              "Talking of Michaelangelo."],
                   'genre': 'modernist'}

burns_rose = {'lyrics': ["O my Luve's like a red, red rose,",
                         "That's newly sprung in June:",
                         "O my Luve's like the melodie,",
                         "That's sweetly play'd in tune."],
              'genre': 'romantic'}

user = raw_input("Who am I impossibly communicating with? > ")
person = Human(user)
print "%s, what is your general situation regarding consciousness and significance?" % person.name 
person.think()
print person.condition

the_poem = Poem(alfred_prufrock['lyrics'], alfred_prufrock['genre'])
the_poem.poetry()
print "###"
print the_poem.genre
print "<>" * 10
the_poem = Poem(burns_rose['lyrics'], burns_rose['genre'])
the_poem.poetry()
print "###"
print the_poem.genre
print "-" * 10
the_poem = Poem(['not the correct lyrics', ' not correct at all.'], 'pathetic')
the_poem.poetry()
print "###"
print the_poem.genre

