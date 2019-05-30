#!/usr/bin/env python3.7
import time

# queue is a list of things to do like youtube's watch later
queue = ["revise anki flashcards",
        "read lectures 5, 6, 7, 7 (other)",
        "make flaschards for convolutions",
        "sign contract",
        "read article about skating australia",
        "fix skateboard",
        "get whatsapp working",
        "watch long trecks on skate decks"]

cache = []

# suggest returns True if the suggestion has been accepted
def suggest(suggestion):
    # valid only takes input that has been converted to lower case
    valid = {"yes": True, "y": True, "no": False, "n": False}

    response = input(suggestion + "? [Y/n]\n")
    return(valid[response.lower()])

# suggest last element in list
# if suggestion accepted, pop it from the stack and never think about it again
# if not accepted, put it in the front of the stack
while(True):
    suggestion = queue[-1]
    accepted = suggest(suggestion)

    if accepted:
        queue.pop()
    else:
        queue[0] = queue.pop()
        cache.append(suggestion)
    else:
        queue[0] = queue.pop()
    print(cache)
    print(queue)
    time.sleep(3)
