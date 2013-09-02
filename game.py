from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "not implemented yet."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class death(Scene):

    quips = [
        "Tough nuts, Charlie Brown.  You're dead.",
        "We all have to go sometime.",
        "Better luck the next 10,000 times.",
        "Don't worry, the Wheel of Samsara turns endlessly, you'll get back here eventually.",
        "I guess it beats a day job."]

    def enter(self):
        print death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class opening_act(Scene):

    def enter(self):
        print """It was a dark and stormy night off the coast of Madagascar.  The Malaysian sailors stabbed one of the Hakka while he was mending the topsail two nights before.  Since that evening it was all Josue could do to keep full-fledged chaos from reigning from rum ration to third watch.  No further blood spilled on the Trinidade in the intervening hours, but the Mate could smell it on the salt spray.  Any time now.

The Captain hadn't left his cabin in a week.  Scurvy, plus the added touch of Cape Fever brought him low in Elizabethtown, and he wasn't a strong specimen to begin with.  Some second son of a Mediera banker on the same hopeless path as every other unlucky boy written out of a will.  Josue knew the man would die before Madras, if not by Karachi.  Which would leave him in charge of this mess.  As if he wasn't already.

You absorb all this in a moment's glance as he levels his brow at you and asks:\n\nSecond or Third Watch?"""

        answer = raw_input("Which watch do you wnat to take tonight? > ")
        answer = answer.upper()

        while not (answer == "SECOND" or answer == "THIRD"):
            print "Enough stalling...tell me plainly: Second or Third."
            answer = raw_input("Which watch do you want to take tonight? > ")
            answer = answer.upper()

        if answer == "SECOND":
            return 'second_watch'

        elif answer == "THIRD":
            return 'third_watch'


class second_watch(Scene):

    def enter(self):
        print "\nYou choose the second watch and Josue heads below to sleep."
        print "All is quiet until around nine bells when you hear approaching"
        print "steps."
        print "You turn to confront the stalker, to find a short jack looking at you."
        print "He says: \"There will be death tonight if you don't act.\""
        print "\"You must come below if you want the captain to live.\""

        answer = raw_input("Do you follow the man below? (yes/no)> ")
        answer = answer.upper()

        while not (answer == "YES" or answer == "NO"):
            print "You can't sit here all night, do you go below?"
            answer = raw_input("(yes/no) > ")
            answer = answer.upper()

        if answer == "NO":
            print "Your strong sense of responsibility and cowardice forces you to "
            print "remain on deck for the rest of your watch.  At nigh to eleven "
            print "bells a strange mist envelops the deck about you.  You never "
            print "see the hand, but the knife it wields slides sharply between"
            print "your fifth and sixth ribs.  As life ebbs away, you hear Joshue's"
            print "voice: \"He never would've joined us...he was a sheep.\""
            return 'death'

        elif answer == "YES":
            print "You summon your courage and nod to the small man.  He turns and"
            print "leads you down the creaking ladder into the darkness of the"
            print "musty hold below."
            return 'below_decks'

class third_watch(Scene):

    def enter(self):
        print "There isn't a soul on deck at this hour, and the sea is raging"
        print "around you.  Banshee shrieks whip through the rigging and their"
        print "ghostly forms dance from sheet to sheet.  Pacing aft towards the"
        print "cabins, you hear a heavy tread amidships.  Whirling to the sound you"
        print "see the glint of a sabre's steel, and behind that the face of Josue,"
        print "intense in the scanty lantern light.  \"I'm going into the Captain's"
        print "cabin,\" he says, \"don't try to stop me.\""

        answer = raw_input("Do you try to stop him? (yes/no) > ")
        answer = answer.upper()

        while not (answer == "YES" or answer == "NO"):
            print "It's kind of a crucial moment, you should probably decide..."
            answer = raw_input("(yes/no) > ")
            answer = answer.upper()

        if answer == "YES":
            print "Without a word, you slowly slide your gleaming sabre from it's"
            print "sheath.  You see the slightest flicker of a smile on Josue's"
            print "lips as he lunges towards you."
            return 'fight'

        elif answer == "NO":
            print "Obedience and self-preservation have always been your greatest"
            print "virtues, and you've fenced with Josue enough to know your odds"
            print "aren't great.  You let him pass, and at a sign from the mate,"
            print "you turn and follow him into the cabin."
            return 'captains_cabin'

class below_decks(Scene):

    def enter(self):
        print "The press of men below is made worse by the pitching of the ship."
        print "The small man leads you aft to the better bunks where you find"
        print "Josue dealing cards on a bulkhead.  \"I need to know something.\""
        print "\"As second mate, would you do anything to save the life of our"
        print "dear captain?  That is, can I trust you in a deed that well"
        print "could decide his fate?\""

        answer = raw_input("Will you accept this task from Josue? (yes/no) > ")
        answer = answer.upper()

        while not (answer == "YES" or answer == "NO"):
            print "Everyone in the hold is looking at you...better answer him."
            answer = raw_input("(yes/no) > ")
            answer = answer.upper()

        if answer == "NO":
            print "You look around at the scarred and poxy faces of the crew."
            print "These men don't look too interested in ensuring the"
            print "safe delivery of the Company's cargo.  They look more apt"
            print "to dump you, Josue and the Captain in the sea and make sail"
            print "for the Gulf of Aden.  You look Josue in the eyes and shake"
            print "your head.  He nods, and quick as a flash, his dirk flies"
            print "from his waistcoat and buries itself to the hilts in your"
            print "throat.  You hear him shout \"Death to mutineers and long-"
            print "live the Company!\" as he lays about with his cutlass.  You"
            print "never know if he survives the melee as you shuffle off this"
            print "mortal coil in a pool of blood and tar."
            return 'death'

        if answer == "YES":
            print "You grasp Josue by the forearm in order to show the fervor"
            print "of your commitment to Captain and Company.  Josue says,"
            print "\"I knew I could count on your loyalty.  Go above and"
            print "finish your watch.\"  You retreat aforeship to the gangway"
            print "feeling understandably unsettled about the whole thing."
            return 'third_watch'


class fight(Scene):

    def enter(self):

        direction = ['LEFT', 'RIGHT']

        answer = raw_input("Josue thrusts at you...do you parry left or right? > ")
        answer = answer.upper()
        josue_action = direction[randint(0,1)]

        if answer == josue_action:
            print "You parry %s and escape his thrust." % answer.lower()
        elif answer != josue_action:
            print "You parry %s and Josue thrusts %s, and that, my friend, is the story of you." % (answer.lower(), josue_action.lower())
            return 'death'
        else:
            print "Your indecision and incompetence leave you vunerable for a moment and Josue thrusts %s and spears you like a hog." % josue_action.lower()
            return 'death'

        answer = raw_input("You've parried, now thrust (left or right) > ")
        answer = answer.upper()
        josue_action = direction[randint(0,1)]

        if answer == josue_action:
            print "You thrust %s and Josue parries." % answer.lower()
            return 'fight'
        elif answer != 'LEFT' and answer != 'RIGHT':
            print "You swing wildly and without any direction."
            print "Josue laughs and steps away marveling at your"
            print "incompetence.  He then poises to strike..."
            return 'fight'
        else:
            print "You thrust %s and Josue foolishly parries %s." % (answer.lower(), josue_action.lower())
            print "Josue crumples to the deck and you turn to"
            print "the Captain's cabin."
            global josue_alive
            josue_alive = False
            return 'captains_cabin' 
           


class captains_cabin(Scene):

    def enter(self):

        if josue_alive == True:
            print "Josue pushes the door open and the stench of mortality"
            print "overwhelms you.  You sink to your knees by the Captain's"
            print "bunk to find his body rapidly cooling.  Josue turns to you"
            print "and says, \"I couldn't take the risk of letting the crew"
            print "know of the Captain's demise without knowing your loyalty."
            print "We will continue on to the Far East, but I will Captain"
            print "and you will be my First Mate, and when we return to Porto"
            print "you will be commissioned in the Company.  Congratuilations."
            print 'finished'
            exit(1)
        elif josue_alive == False:
            print "You enter the cabin to find a blunderbuss leveled straight"
            print "at your nose.  The Captain is shaking and demands: \"Have"
            print "you come to kill me?\""

            answer = raw_input("Do you want to kill the Captain? (yes/no) > ")
            answer = answer.upper()

            while not (answer == "YES" or answer == "NO"):
                print "He looks impatient, you'd better answer."
                answer = raw_input("(yes/no) > ")
                answer = answer.upper()

            if answer == "NO":
                print "The Captain looks wryly at you and then to your bloodied"
                print "sabre.  \"Oh no?\" he says, \"Then I suppose you've just"
                print "helping Duncan butcher hogs in the mess, eh?\"  The Captain"
                print "then sees Josue's body lying on the deck. \"Perfidy!\""
                print "\"Mutiny!!\" he screams as the roar of powder fills your"
                print "ears and a ball enters your brain."
                return 'death'
            if answer == "YES":
                print "You look contemptuously at the quivering mold of clay"
                print "lying before you in its soiled sheets and are put in mind"
                print "of the recent writings of the Englishman, Charles"
                print "Darwin.  With a flick of your sabre you knock the"
                print "gunbarrel aside just as the Captain pulls the trigger."
                print "The ball sinks deep into the beam by your shoulder, but"
                print "you remain unscathed.  The fear in the Captain's eyes"
                print "is laughable, but you're in no mood for humor.  A quick"
                print "thrust and you have risen in rank to Captain.  At least"
                print "for now.  Perhaps rather than try to convince the"
                print "Company that you've come to your new station through"
                print "the purest of motives, it migh tbe a better idea to try"
                print " a little piracy in the South Seas.  Either way, it's"
                print "better than taking orders, right?"
                print 'finished'
                exit(1)


class Map(object):

    scenes = {
        'opening_act': opening_act(),
        'second_watch': second_watch(),
        'third_watch': third_watch(),
        'below_decks': below_decks(),
        'fight': fight(),
        'captains_cabin': captains_cabin(),
        'death': death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


josue_alive = True
a_map = Map('opening_act')
a_game = Engine(a_map)
a_game.play()
