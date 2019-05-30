#!/usr/bin/env python3.7

# queue is a list of things to do like youtube's watch later
queue = ["revise anki flashcards",
        "read lectures 5, 6, 7, 7 (other)",
        "make flaschards for convolutions",
        "sign contract",
        "read article about skating australia",
        "fix skateboard",
        "get whatsapp working",
        "watch long trecks on skate decks"]

suggestion = queue[-1]
# suggest last element in list

# suggest returns True if the suggestion has been accepted
def suggest(suggestion):
    # valid only takes input that has been converted to lower case
    valid = {"yes": True, "y": True, "no": False, "n": False}

    response = input(suggestion + "? [Y/n]\n")
    return(valid[response.lower()])
print(suggest(suggestion))
