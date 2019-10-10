"""
Module: comp110_lab06

Exercises from lab 06, dealing with string accumualators.
"""

import sound

def create_sound(sound_string):
    """ 
    Function that uses sound_string to create a sound object.
    Each character is either a letter signifying a note
    (a, b, c, d, e, f, g, each could be upper or lower case), or
    a single digit number (1, 2, 3, 4, 5, 6, 7, 8, 9), or s to indicate
    a silent sound. 

    The function should create and return a sound object consisting
    of the notes specified in the string (in the same order as they
    appear in the string.)  Each note should be inserted into the sound
    object for one half second, and it should be at the default octave.  
    If, however, the character before a note is a digit, then the note should
    appear for longer. For example, if the digit is 4, then the next note
    should be inserted with a length of 4 times one half second, or 2 seconds.
    """

    return None   # replace this when you're done.

# Do not modify anything after this point.
if __name__ == "__main__":
    snd = create_sound("3Eabcde2Sc2e2Sc2egacadca")
    snd.play()
    sound.wait_until_played()