#!/usr/bin/env python3.7
import time 

# queue is a list of things to do like youtube's watch later
with open('queue', 'r+') as f:
    queue = f.read().splitlines()
print(queue)

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
    suggestion = -1
    accepted = suggest(queue[suggestion])

    if accepted:
        cache.append(queue[suggestion])
        queue.pop(suggestion)
    else:
        queue[0] = queue.pop(suggestion)
    print(cache)
    print(queue)
    time.sleep(3)
