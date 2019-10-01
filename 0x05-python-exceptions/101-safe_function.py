#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        p = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        p = None
    return p
