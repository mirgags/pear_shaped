print """It was a dark and stormy night off the coast of Madagascar.  The Malaysian sailors stabbed one of the Hakka while he was mending the topsail two nights before.  Since that evening it was all Josue could do to keep full-fledged chaos from reigning from rum ration to third watch.  No further blood spilled on the Trinidade in the intervening hours, but the Mate could smell it on the salt spray.  Any time now.

The Captain hadn't left his cabin in a week.  Scurvy, plus the added touch of Cape Fever brought him low in Elizabethtown, and he wasn't a strong specimen to begin with.  Some second son of a Mediera banker on the same hopeless path as every other unlucky boy written out of a will.  Josue knew the man would die before Madras, if not by Karachi.  Which would leave him in charge of this mess.  As if he wasn't already.

You absorb all this in a moment's glance as he levels his brow at you and asks:\n\nSecond or Third Watch?"""

answer = raw_input("Which watch do you wnat to take tonight?")
answer = answer.upper()

while not (answer == "SECOND" or answer == "THIRD"):
    print "Enough stalling...tell me plainly: Second or Third."
    answer = raw_input("Which watch do you want to take tonight?")
    answer = answer.upper()

if answer == "SECOND":
    print "\nPussy"
    print "\nSometime around 9 at night you slip on a banan peel and fall in the Arabian Sea, never to be seen again.  Later"
elif answer == "THIRD":
    print "\nOkay, watch your back."
    print "\nAn hour before dawn the storm turns grizzly and lightning strikes you as you lift your sabre to block the swift downcut of an Antiguan cook's cleaver.  Donezo."
 

