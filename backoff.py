#!/usr/bin/env python3.7
import time 

# queue is a list of things to do like youtube's watch later
with open('queue', 'r+') as f:
    queue = f.read().splitlines()

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
# while there are things to suggest in the queue
while queue:
    # start from the end
    index = -1
    accepted = suggest(queue[index])

    if accepted:
        cache.append(queue[index])
        queue.pop(index)
    else:
        queue[0] = queue.pop(index)
    time.sleep(3)
