"""First hug API (local and HTTP access)"""
import hug
from _functions import forward, backwards

delay = 0.02

@hug.get()
@hug.local()
def camera(rotate: hug.types.smart_boolean, steps: hug.types.number, dir: hug.types.smart_boolean):
    """Move the pan/tilt head"""
    if dir == 0:
        forward(delay, steps, rotate)
        return {'0'}
    else:
        backwards(delay, steps, rotate)
        return{'1'}
    