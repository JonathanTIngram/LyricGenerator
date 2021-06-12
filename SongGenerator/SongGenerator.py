import random
import tkinter
from tkinter import *


class Word:

    def noun():
        with open("nouns.txt", "r") as n:
            nouns = n.readlines()

        return (random.choice(nouns))

    def verb():
        with open("verbs.txt", "r") as v:
            verbs = v.readlines()

        return (random.choice(verbs))

    def adj():
        with open("adj.txt", "r") as a:
            adjs = a.readlines()

        return (random.choice(adjs))

    def adverb():
        with open("adverbs.txt", "r") as ad:
            adverbs = ad.readlines()

        ly = random.choice(adverbs)

        return (ly)
        
def new_lyric():

    adj = Word.adj()
    noun = Word.noun()
    noun2= Word.noun()
    verb = Word.verb()
    
    endOfVerb = verb[len(verb.strip()) - 1]

    lyric = ""

    if(endOfVerb == 'e'):
        verb = verb.strip() + "d"
        lyric = ("The " + adj + 
            " " + noun + " " + 
            verb + " the " + 
            noun)
    elif(endOfVerb == 'y' and
         endOfVerb != 'ay' and
         endOfVerb != 'ey' and
         endOfVerb != 'iy' and
         endOfVerb != 'oy' and
         endOfVerb != 'uy'):
        
        endOfVerb.strip().replace("y", "")
        verb = verb.strip() + "ied"

        lyric = ("The " + adj + 
                 " " + noun + " " +
                 verb + " the " +
                 noun2)
    


    else:
        verb = verb.strip() + "ed"
        lyric = ("The " + adj + 
        " " + noun + " " + 
        verb + " the " + 
        noun2)

    return lyric


